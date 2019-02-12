# coding: utf-8

from datetime import datetime, date, timedelta
from os import path
import random
import os
import sys

from faker import Faker
fake = Faker()

AUTHOR = 'Adam Tegtmeier'
EMAIL = 'ategtmei@gmail.com'
DAYS_TO_GENERATE = 365

shell_path = r"C:\Program Files\Git\bin\sh.exe"
truncated_shell_path = shell_path.replace("C:\\Program Files","P:")

def dateMinusGivenDays(days):
    return date.today() - timedelta(days=days)

def psudorandom_datetime(date):
    return datetime(year=date.year, month=date.month, day=date.day, hour=random.randint(0,23), minute=random.randint(0, 59), second=random.randint(0, 59))

def touchFile(path):
    with open(path, 'ab') as handle:
        handle.write(os.linesep.encode())
        handle.write(str(random.random()*10).replace('.','').encode())

def setup(path_to_cheat_repo):
    initial_dir = os.getcwd()
    os.system("subst P: \"C:\\Program Files\"")
    os.chdir(path_to_cheat_repo)
    return initial_dir

def tearDown(initial_dir):    
    os.system("subst P: /D")
    os.chdir(initial_dir)

def makeCommitInPast(fake_datetime, message):
    special_command = f"GIT_AUTHOR_DATE='{fake_datetime.isoformat()}' GIT_COMMITTER_DATE='{fake_datetime.isoformat()}' git commit --author='{AUTHOR} <{EMAIL}>' -m '{message}'"
    special_command = special_command.replace("'",'"')
    return os.system(f"{truncated_shell_path} -c '{special_command}'")

def addChange(base_name):
    return os.system(f"\"{shell_path}\" -c 'git add {base_name}'")

def pullADateFromHistory(limitDaysPast):
    daysAgo = random.randint(0, limitDaysPast)
    fake_date = dateMinusGivenDays(daysAgo)
    fake_datetime = psudorandom_datetime(fake_date)
    return fake_datetime

def isWeekEnd(datetime):
    wkday = datetime.strftime('%a')
    return wkday in {'Sun', 'Sat'}

def psudo_date(limitDaysPast, weekends = False):
    for _ in range(500):
        history = pullADateFromHistory(limitDaysPast)
        if weekends or not isWeekEnd(history):
            return history

def createCommitInPast(file, fake_datetime, message):
    touchFile(file)
    addChange(file)
    makeCommitInPast(fake_datetime, message)

def execute(count, dirname, file = 'time', day_limit = DAYS_TO_GENERATE):
    initial_dir = setup(dirname)
    for _ in range(count):
        mostly_random_date = psudo_date(day_limit)
        createCommitInPast(file, mostly_random_date, fake.text().replace('\n',' '))

    tearDown(initial_dir)

if __name__ == '__main__':
    execute(int(sys.argv[1]), sys.argv[2] if len(sys.argv) > 2 else '.')