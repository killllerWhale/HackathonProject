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
    con = pymysql.connect(host='localhost', user='root', password='nlp2', database='books')
    cur = con.cursor()
    cur.close()
    with open("books.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=",")
        for row in file_reader:
            for elem in range(len(row)):
                cur = con.cursor()
                if len(row[1].split()) > 13:
                    if elem == 0:
                        sql =("INSERT INTO book (book_name, book_desc) VALUES(%s,%s);")
                        cur.execute(sql, (row[elem], row[elem+1]))
                        cur.close()
    con.commit()
    con.close()


parsi()
