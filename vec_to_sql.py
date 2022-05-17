import re
import nltk
import csv
from multiprocessing import cpu_count
from gensim.models import doc2vec
from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec
import pymorphy2
import pymysql


con = pymysql.connect(host='localhost', user='root', password='nlp2', database='books')

with con:
    cur = con.cursor()


def parsi():
    # with open("books.csv", encoding='utf-8') as r_file:
    #     # Создаем объект reader, указываем символ-разделитель ","
    #     file_reader = csv.reader(r_file, delimiter = ",")
    #     # Считывание данных из CSV файла
    #     model_string = ""
    #     for row in file_reader:
    #         for elem in row:
    #             model_string += elem + " "
    #     processed_article = model_string.lower()
    #     processed_article = re.sub('[^a-zA-ZА-я]', ' ', processed_article)
    #     processed_article = re.sub(r'\s+', ' ', processed_article)
    #     # создаем модель для распознавания
    #     all_sentences = nltk.sent_tokenize(processed_article)
    #     all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
    #     w2v_model = Word2Vec(all_words, min_count=0, workers=cpu_count())

    # Создаем массив векторов описания
    with open("books.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            for elem in range(len(row)):
                if len(row[1].split()) > 13:
                    if elem == 0:
                        cur.execute(f"INSERT INTO book (book_name) VALUE({row[elem]});")
                    else:
                        cur.execute(f"INSERT INTO book (book_desc) VALUE({row[elem]});")

    cur.close()


parsi()
