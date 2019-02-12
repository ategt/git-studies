# coding: utf-8

import subprocess
import uuid
import re

from github_cheater import shell_path, truncated_shell_path, setup, tearDown


regex = re.compile("commit (?P<hash>[0-9a-f]*)(?P<branch> \(.+\))?\\nAuthor: (?P<author>(?:\w| )*)<(?P<email>(?:\w|@|\.)*)>\\nDate:(?: )*(?P<datetime>(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun) (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (?:\d)+ (?:\d)+:(?:\d)+:(?:\d)+ (?:\d)+ (?:\-|\+|\d)+)")
current_guid = uuid.uuid4().hex

def git_log_from_repo(repo_path):
    inital_dir = setup(repo_path)
    log_string = subprocess.Popen(f"\"{shell_path}\" -c 'git log -a'", shell=True, stdout=subprocess.PIPE).stdout.read()
    tearDown(inital_dir)

    return log_string

def handle_item(match, lst4):
    lst4.append(match.groupdict())
    return current_guid

def parse_log(log_string):
    lst4 = []
    local_handle_item = lambda m: handle_item(m, lst4)
    matches = regex.sub(local_handle_item, log_string.decode())

    commits = [{**item, 'message': messages[1:][idx].strip()} for idx, item in enumerate(lst4)]

    return commits
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\others\python\assorted-python")
import os
os.getcwd()
commits = parse_log(log_string)
def parse_log(log_string):
    lst4 = []
    local_handle_item = lambda m: handle_item(m, lst4)
    matches = regex.sub(local_handle_item, log_string.decode())

    messages = matches.split(current_guid)

    commits = [{**item, 'message': messages[1:][idx].strip()} for idx, item in enumerate(lst4)]

    return commits
commits = parse_log(log_string)
len(commits)
commits[]
commits[0]
branches = list(filter(lambda x: x['branch'] is not None, commits))
len(branches)
def git_log_from_repo(repo_path):
    inital_dir = setup(repo_path)
    log_string = subprocess.Popen(f"\"{shell_path}\" -c 'git log --all'", shell=True, stdout=subprocess.PIPE).stdout.read()
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
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\others\python\assorted-python")
commits = parse_log(log_string)
branches = list(filter(lambda x: x['branch'] is not None, commits))
len(branches)
len(commits)
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\canvas")
commits = parse_log(log_string)
len(commits)
commits[0]
log_string.decode()[:900]
commits[0]
def git_log_from_repo(repo_path):
    inital_dir = setup(repo_path)
    log_string = subprocess.Popen(f"\"{shell_path}\" -c 'git log --all --decorate'", shell=True, stdout=subprocess.PIPE).stdout.read()
    tearDown(inital_dir)

    return log_string
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\canvas")
commits = parse_log(log_string)
len(commits)
branches = list(filter(lambda x: x['branch'] is not None, commits))
len(branches)
branches[0]
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\guild-self-work")
commits = parse_log(log_string)
len(commits)
guild_self = commits
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
commits = parse_log(log_string)
len(commits)
guild_group_project = commits
#guild_group_project
import pandas as df
ggp = df(guild_group_project)
ggp = df.DataFrame(guild_group_project)
len(ggp.author)
ggp.author[5]
log_string = git_log_from_repo(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
commits = parse_log(log_string)
len(commits)
def load_git_df(path):
    log_string = git_log_from_repo(path)
    commits = parse_log(log_string)

    return (commits_to_df, len(commits))
ggp, lx = load_git_df(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
lx
def commits_to_df(commits):
    return df(commits)
ggp, lx = load_git_df(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
lx
from collections import Counter
Counter(ggp['author'])
ggp['author']
ggp[author]
ggp['author']
ggp.head(3)

def load_git_df(path):
    log_string = git_log_from_repo(path)
    commits = parse_log(log_string)

    return (commits_to_df(commits), len(commits))
ggp, lx = load_git_df(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
lx
from pandas import DataFrame as df
ggp, lx = load_git_df(r"C:\Users\ATeg\Documents\_repos\guild-group-project")
lx
ggp.head(3)
Counter(ggp['author'])
ggp['message'][0]
Counter(ggp['email'])
ggp['date'][0]
ggp.head(3)
ggp['datetime'][0]
from datetime import datetime
datetime.now()
d = datetime.now()
d.strftime('%a')
d.strftime('%a %M')
d.strftime('%a %m %M')
d.strftime('%c %z')
dts = ggp['datetime']
edts = [datetime.strptime(input_str, '%c %z') for input_str in dts]
edts[4]
ggp['parsed_date'] = edts
ggp.head(3)
#edts['parsed_date']
ggp['date'] = [dt.date for dt in ggp['parsed_date']]
ggp['time'] = [dt.time for dt in ggp['parsed_date']]
ggp['time'][9]
ggp['time'][9]()
ggp['time'] = [dt.time() for dt in ggp['parsed_date']]
ggp['date'] = [dt.date() for dt in ggp['parsed_date']]
ggp['time'][9]
ggp['time'][17]()
ggp['time'][17]
from datetime import timedelta
datetime.time(9,0,0)
import time
time.time()
time.time(hour=8)
datetime.time(9,0,0)
datetime.timetuple()
ggp['time'][17]
ggp['time'][17].timetuple()
datetime.timetuple()
ggp['time'][17]
datetime.time(17, 49, 4)
help(datetime.time)
datetime.time()
datetime.time(57)
datetime.time(datetime.now())
datetime.time(datetime.now())
datetime.time(datetime.now())
datetime.datetime(year=2018,month=10,day=18)
datetime(year=2018,month=10,day=18)
datetime(year=2018,month=10,day=18, hour=9,minute=0,second=0)
datetime(year=2018,month=10,day=18, hour=9,minute=0,second=0).time()
nine = datetime(year=2018,month=10,day=18, hour=9,minute=0,second=0).time()
ggp['time'][17]
ggp['time'][17] - nine
ggp['time'][17]
tx = ggp['time'][17]
tx.hour
tx.hour 
tx.hour > 9
def hoursSince(tx):
    if tx.hour > 9:
        return tx.hour - 9
    else:
        return tx.hour + 15
    
hoursSince(ggp['time'][17])
hoursSince(ggp['time'][98])
def hoursSince(tx, base):
    if tx.hour > base:
        return tx.hour - base
    else:
        return tx.hour + (24-base)
    
    
def hoursSince(tx, base = 9):
    if tx.hour > base:
        return tx.hour - base
    else:
        return tx.hour + (24-base)
    
hoursSince(ggp['time'][98])
ggp['date'][99]
dx = ggp['date'][99]
dx.strftime('%a')
ggp['elapsed'] = [hoursSince(dt.time(), 15 if dt.strftime('%a') == 'Sun' else 9) for dt in ggp['parsed_date']]
ggp['elapsed'][8]
max(ggp['elapsed'])
bgx = ggp.loc[ggp['elapsed']>20]
len(bgx)
bgx.head(5)
ggp[100]
ggp.index
ggp.index[100]
ggp.iloc[100]
ggp.iloc[100]['parsed_date']
ggp.iloc[100]['parsed_date'].time()
ggp.iloc[100]['parsed_date'].time().strftmie('%c')
ggp.iloc[100]['parsed_date'].time().strftime('%c')
ggp.iloc[100]['parsed_date'].time().strftime('%z')
ggp.iloc[100]['parsed_date'].time().strftime('%c')
ggp.iloc[100]['parsed_date'].time().strftime('%p')
ggp.iloc[100]['parsed_date'].time().strftime('%h %p')
ggp.iloc[100]['parsed_date'].time().strftime('%H %p')
ggp.iloc[100]['parsed_date'].time().strftime('%t %p')
ggp.iloc[100]['parsed_date'].time().strftime('%T %p')
ggp.iloc[100]['parsed_date'].time().strftime('%I %p')
ggp.iloc[100]['parsed_date'].time().strftime('%I %p - %T')
ggp.iloc[100]['parsed_date'].time().strftime('%I %p - %T')
12-9
4
hoursSince(ggp.iloc[100]['parsed_date'].time(), 15 if ggp.iloc[100]['parsed_date'].strftime('%a') == 'Sun' else 9)
hoursSince(ggp.iloc[100]['parsed_date'].time(), 9)
hoursSince(ggp.iloc[100]['parsed_date'].time(), 15)
ggp.iloc[100]['parsed_date'].time().strftime('%I %p - %T')
15-13
def hoursSince(tx, base = 9):
    if tx.hour > base:
        return tx.hour - base
    else:
        return tx.hour + (24-base)
    
24-15
9+9
24-15
13+9
bgx.head(5)
def hoursSince(tx, base = 9):
    if tx.hour >= base:
        return tx.hour - base
    else:
        return tx.hour + (24-base)
    
ggp['elapsed'] = [hoursSince(dt.time(), 15 if dt.strftime('%a') == 'Sun' else 9) for dt in ggp['parsed_date']]
bgx = ggp.loc[ggp['elapsed']>20]
bgx.head(5)
len(bgx)
bgx.head()
bgx
bgx = ggp.loc[ggp['elapsed']>15]
bgx = ggp.loc[ggp['elapsed']>20]
bgx2 = ggp.loc[ggp['elapsed']>15]
len(bgx2)
bgx2 = ggp.loc[ggp['elapsed']>14]
len(bgx2)
bgx2 = ggp.loc[ggp['elapsed']>12]
len(bgx2)
bgx2
bgx2 = ggp.loc[ggp['elapsed']>12 && ggp['elapsed']< 20]
bgx2 = ggp.loc[ggp['elapsed']>12 and ggp['elapsed']< 20]
reals = ggp.loc[ggp['elapsed']<20]
bgx2 = ggp.loc[reals['elapsed']>10]
bgx2 = reals.loc[reals['elapsed']>10]
len(bgx2)
bgx2
bgx2[['author','datetime','elapsed']]
get_ipython().run_line_magic('save', 'git_analyzer 0-181')
