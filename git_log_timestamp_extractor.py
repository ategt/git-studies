import sys, re
from datetime import datetime, timedelta
from collections import Counter

commits = []
commit = {}

for line in sys.stdin:
	if re.match('commit', line):
		if commit:
			commits.append(commit)
		commit = {'message':''}
		commit_hash = re.split(' ', line)[1]
		commit['hash'] = commit_hash

	if re.match('Author', line):
		author = line.split(':')[1].strip()
		commit['author'] = author

	if re.match('Date', line):
		date = line.split('e:')[1].strip()
		date = datetime.strptime(date, '%c %z')
		commit['date'] = date

	if re.match('\W+.+', line):
		commit['message'] += line

print("Total Commits: {}".format(len(commits)))

counter = Counter([i['author'] for i in commits])
for user in counter:
     print('{}:\t{}'.format(user, counter[user]))

#print(commits[0:10])

my_commits = [filtered_commit for filtered_commit in commits if re.search('Tegtmeier', filtered_commit['author'])]

print()
print('--------------')
print("My Commits: {}".format(len(my_commits)))

#print(my_commits[0:10])
print()

dates = [ i['date'] for i in my_commits]
days_bucket_counter = Counter([bday.strftime('%m %d %Y') for bday in dates])
days_bucket = [i for i in days_bucket_counter.items()]

for i in days_bucket:
	print("%s : %s" % (i[0], i[1]))











days_dict = {}

times = [(bday.strftime('%m %d %Y'), bday.strftime('%X')) for bday in dates]

date_set = set()
for date_time_tuple in times:
    date_set.add(date_time_tuple[0])

date_times = {}
for date_time in date_set:
    date_times[date_time] = []

for i in times:
    time_list = date_times[i[0]]
    time_list.append(i[1])
    date_times[i[0]] = time_list

max_day_time = {}
for i in date_times:
    day = i
    time_list = date_times[i]
    max_time = max(time_list)
    max_day_time[day] = max_time

print()
print('Latest Commits:')
for i in max_day_time:
	hour_str = re.split(':', max_day_time[i])
	hours = int(hour_str[0])
	corrected_hours = hours - 9
	print("%s : %s - %s" % (i, max_day_time[i], "{}:{}:{}".format(corrected_hours, hour_str[1], hour_str[2])))

	