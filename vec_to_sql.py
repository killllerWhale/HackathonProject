import re
import nltk
import csv
from multiprocessing import cpu_count
from gensim.models import doc2vec
from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec
import pymorphy2
import pymysql


def parsi():
    con = pymysql.connect(host='88.135.126.54', user='slava', password='nlp2', database='books', port=3306)
    cur = con.cursor()
    cur.close()
    with open("books.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            for elem in range(len(row)):
                cur = con.cursor()
                if len(row[1].split()) > 13:

    con.commit()
    con.close()


parsi()
