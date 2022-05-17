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
from gensim.models.doc2vec import Doc2Vec, LabeledSentence


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


TaggedDocument = gensim.models.doc2vec.TaggedDocument

# Читать и обрабатывать данные
def get_datatset(sentences):
    all_sentence = []
    for i, sentence in enumerate(sentences):
        all_sentence.append(TaggedDocument(sentence.split(), tag=[i]))
    return all_sentence


# Получить текстовый вектор из набора данных.
def getVecs(model, corpus, vector_size):
    vecs = [np.array(model.docvecs[z.tags[0]].reshape(1, vector_size)) for z in corpus]
    return np.concatenate(vecs)


# Тренируйте модель с текстом набора данных
def train(all_sentence, vector_size, min_count, epoch):
    model = Doc2Vec(vector_size=vector_size, min_count=min_count, epochs=epoch)
    model.build_vocab(all_sentence)
    model.train(all_sentence, total_examples=model.corpus_count, epochs=model.epochs)
    return model


def similarity(model):
    test_text = 'xxx xxx xxxxx'.split()
    inferred_vector = model.infer_vector(test_text)
    sims = model.most_similar([inferred_vector], topn=10)
    return sims




#
# # Для обучения модели нам нужен список целевых документов
# def tagged_document(list_of_ListOfWords):
#     for x, ListOfWords in enumerate(list_of_ListOfWords):
#         yield doc2vec.TaggedDocument(ListOfWords, [x])
#
#
# # тренировочные данные
# data_train = list(tagged_document(book_desc))
#
# # вывести обученный набор данных
# print(data_train[:1])

#print(book_desc)
# print(book_name)




