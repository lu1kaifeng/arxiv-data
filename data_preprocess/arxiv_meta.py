import re
from tqdm import tqdm
filename = re.compile(r'(.*)\.txt')
with open('../data/arxiv_tuple_pickle', 'rb') as f:
    import pickle

    d = pickle.load(f)
    names = []
for (_, name) in tqdm(d):
    name = filename.match(name).group(1)
    names.append(name)
del d
with open('../data/arxiv-metadata-oai-snapshot.json', 'r') as f:
    import json

    objs = []
    for li in tqdm(f):
        obj = json.loads(li)
        if obj['id'] in names:
            objs.append(obj)
with open('../data/arxiv-metadata_pickle', 'wb') as f:
    pickle.dump(objs, f)
