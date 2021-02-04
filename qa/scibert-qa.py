from transformers import AutoTokenizer, AutoModel,AutoModelForQuestionAnswering
import torch

tokenizer = AutoTokenizer.from_pretrained("../models/scibert_scivocab_uncased_squad_v2")
model = AutoModelForQuestionAnswering.from_pretrained("../models/scibert_scivocab_uncased_squad_v2")

inputs = tokenizer("Hello world!","Second Sentence!", return_tensors="pt",add_special_tokens=True)
outputs = model(**inputs)
