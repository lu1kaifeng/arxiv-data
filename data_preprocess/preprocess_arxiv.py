import spacy
from tqdm import tqdm

import multiprocessing

the_queue = multiprocessing.Queue()
spacy.require_gpu()
nlp = spacy.load("en_core_sci_sm")
import os

with open(os.path.join('../data', 'arxiv_tuple'), 'r') as f:
    dic = eval(f.read())

processed = nlp.pipe(texts=dic, as_tuples=True, batch_size=8)


def to_file(doc):
    with open(os.path.join('../data/arxiv-processed', doc[1]), 'w') as ff:
        print(list(map(lambda x: x.string, list(doc[0].sents))), file=ff)


for doc in tqdm(processed, total=len(dic)):
    to_file(doc)
