import json
import datetime
import os


def is_cs(s):
    s = s.split()
    is_in = False
    for ss in s:
        is_in = is_in | (ss == 'cs.CV') | (ss == 'cs.CL')
        if is_in:
            print(s)
    return is_in


def in_date_range(t):
    if len(str(t).split('.')) != 2:
        return False
    t, _ = str(t).split('.')
    return datetime.datetime.strptime(t, "%y%d").date() > datetime.date(2017, 1, 1)


with open('../data/arxiv-metadata-oai-snapshot.json') as f:
    data = []
    for l in f:
        data.append(json.loads(l))
data_1 = list(filter(lambda x: is_cs(x['categories']) and in_date_range(x['id']), data))
list = []
for d in data_1:
    list.append((d['id'], d['versions'][len(d['versions'])- 1]['version']))
with open('../data/arxiv_list.txt', 'w') as f:
    print(list, file=f)
