# coding: utf-8

import subprocess
import uuid
import re

from github_cheater import shell_path, truncated_shell_path, setup, tearDown

from pandas import DataFrame as df


regex = re.compile("commit (?P<hash>[0-9a-f]*)(?P<branch> \(.+\))?\\nAuthor: (?P<author>(?:\w| )*)<(?P<email>(?:\w|@|\.)*)>\\nDate:(?: )*(?P<datetime>(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?:\d)+ (?:\d)+:(?:\d)+:(?:\d)+ (?:\d)+ (?:\-|\+|\d)+)")
current_guid = uuid.uuid4().hex

def git_log_from_repo(repo_path):
    inital_dir = setup(repo_path)
    log_string = subprocess.Popen(f"\"{shell_path}\" -c 'git log --all --decorate'", shell=True, stdout=subprocess.PIPE).stdout.read()
    tearDown(inital_dir)

    return log_string

def handle_item(match, lst4):
    lst4.append(match.groupdict())
    return current_guid

def parse_log(log_string):
    lst4 = []
    local_handle_item = lambda m: handle_item(m, lst4)
    matches = regex.sub(local_handle_item, log_string.decode())

    messages = matches.split(current_guid)

    commits = [{**item, 'message': messages[1:][idx].strip()} for idx, item in enumerate(lst4)]

    return commits

def commits_to_df(commits):
    return df(commits)

def load_git_df(path):
    log_string = git_log_from_repo(path)
    commits = parse_log(log_string)

    return (commits_to_df(commits), len(commits))

# branches = list(filter(lambda x: x['branch'] is not None, elst))
# len(branches)
# branches = list(filter(lambda x: x['branch'] is None, elst))
# len(branches)
# branches = list(filter(lambda x: x['hash'] == '116b3f55a2258704dcb51610ebd806b4653478a0', elst))

