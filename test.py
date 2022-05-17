import re
import nltk
import csv
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
import gensim
import gensim.downloader as api
from gensim.models import doc2vec
import sys
import numpy as np
import gensim
from gensim.models.doc2vec import Doc2Vec


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
    # создаем модель для распознавания
    all_sentences = nltk.sent_tokenize(processed_article)
    all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
    w2v_model = Word2Vec(all_words, min_count=0, workers=cpu_count())

#Создаем массив векторов описания
with open("books.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    for row in file_reader:
        for elem in range(len(row)):
            s = row[elem].lower()
            s = re.sub('[^a-zA-ZА-я]', ' ', s)
            s = s.split()
            #temp = []
            if elem == 0:
                book_name.append(row[elem])
            else:
                # for i in range(len(s)):
                #     temp.append(w2v_model.wv[s[i]])
                book_desc.append(row[elem])


# Для обучения модели нам нужен список целевых документов
# def tagged_document(list_of_ListOfWords):
#     for x, ListOfWords in enumerate(list_of_ListOfWords):
#         yield doc2vec.TaggedDocument(ListOfWords, [x])


# тренировочные данные
#data_train = list(tagged_document(book_desc))

# расширить словарный запас
#d2v_model.build_vocab(data_train)

# Обучение модели Doc2Vec
#d2v_model.train(data_train, total_examples=d2v_model.corpus_count, epochs=d2v_model.epochs)

# # Анализ выходных данных
# analyze = d2v_model.infer_vector(['нож', 'студент', 'топор', 'старуха'])
#Запись модели
#d2v_model.save('d2v_Model')
d2v_model = Word2Vec.load('d2v_Model')


def similarity(model):
    test_text = 'Действие происходит в бедном районе Петербурга 1860-х годов. Родион Раскольников, бывший студент, закладывает старухе-процентщице последнюю ценную вещь.'
    test_text = re.sub('[^a-zA-ZА-я]', ' ', test_text)
    test_text = test_text.lower().split()
    inferred_vector = model.infer_vector(test_text)
    sims = model.dv.most_similar([inferred_vector], topn=10)
    for i in range(len(sims)):
        print("----------")
        print(book_name[sims[i][0]], end="\n")
        print(book_desc[sims[i][0]], end="\n")
        print("----------")
    return sims


print(similarity(d2v_model))






