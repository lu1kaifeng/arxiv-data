import os
l=0
for filename in os.listdir('../data/arxiv-processed/'):
    if filename.endswith(".txt"):
        with open(os.path.join('../data/arxiv-processed/', filename),'r') as f:
            obj = eval(f.read())
            for o in obj:
                print(l)
                if len(o['text']) > l:
                    l = len(o['text'])
