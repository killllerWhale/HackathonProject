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

model_string = ""
with open("books.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Считывание данных из CSV файла
    for row in file_reader:
        for elem in row:
            model_string += elem + " "
processed_article = model_string.lower()
processed_article = re.sub('[^a-zA-ZА-я]', ' ',processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)
# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
# #  сохранение извлеченных токенов в словарь
# my_dictionary = corpora.Dictionary(all_words)
# # сохраните словарь на диске
# #my_dictionary.save('my_dictionary.dict')
#
# # загрузите обратно
# load_dict = corpora.Dictionary.load('my_dictionary.dict')
#
# # преобразование в слов Bag of Word
# bow_corpus =[load_dict.doc2bow(doc, allow_update = True) for doc in all_words]
# print(bow_corpus)
w2v_model = Word2Vec(all_words, min_count=0, workers=cpu_count())

# вектор слов для слова "время"

print(w2v_model.wv.most_similar('нож'))

# сохранение и загрузка модели
w2v_model.save('Word2VecModel')
model = Word2Vec.load('Word2VecModel')

