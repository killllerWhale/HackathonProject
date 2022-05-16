import numpy as np
from scipy import spatial
from gensim.models import Word2Vec
import re
import nltk
from gensim import corpora
import csv
import gensim.downloader as api
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)

connections.connect("default", host="localhost", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="book_name", dtype=DataType.FLOAT_VECTOR, dim=8),
    FieldSchema(name="book_desk", dtype=DataType.FLOAT_VECTOR, dim=8)
]

# schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
# hello_milvus = Collection("hello_milvus", schema)
book_name = []
book_desc = []
with open("books.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Считывание данных из CSV файла
    model_string = ""
    for row in file_reader:
        for elem in row:
            model_string += elem + " "
    processed_article = model_string.lower()
    processed_article = re.sub('[^a-zA-ZА-я]', ' ', processed_article)
    processed_article = re.sub(r'\s+', ' ', processed_article)
    # Preparing the dataset
    all_sentences = nltk.sent_tokenize(processed_article)
    all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
    w2v_model = Word2Vec(all_words, min_count=0, workers=cpu_count())

with open("books.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        for elem in range(len(row)):
            s = row[elem].lower()
            s = re.sub('[^a-zA-ZА-я]', ' ', s)
            s = s.split()
            temp = []
            if elem == 0:
                for i in range(len(s)):
                    temp.append(w2v_model.wv[s[i]])
                book_name.append(temp)
            else:
                for i in range(len(s)):
                    temp.append(w2v_model.wv[s[i]])
                book_desc.append(temp)

print(len(book_name))
print(len(book_desc))

# entities = [
#     [i for i in range(len(book_name))],  # field pk
#     book_name,  # field random
#     book_desc,  # field embeddings
# ]
# insert_result = hello_milvus.insert(entities)
#
# index = {
#     "index_type": "IVF_FLAT",
#     "metric_type": "L2",
#     "params": {"nlist": 128},
# }
# hello_milvus.create_index("embeddings", index)
#
# hello_milvus.load()
# vectors_to_search = entities[-1][-2:]
# search_params = {
#     "metric_type": "l2",
#     "params": {"nprobe": 10},
# }
# result = hello_milvus.search(vectors_to_search, "embeddings", search_params, limit=3, output_fields=["random"])
#


# processed_article = row[elem].lower()
# processed_article = re.sub('[^a-zA-ZА-я]', ' ', processed_article)
# processed_article = re.sub(r'\s+', ' ', processed_article)
# all_sentences = nltk.sent_tokenize(processed_article)
# all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
# w2v_model = Word2Vec(all_words, min_count=0, workers=cpu_count())



