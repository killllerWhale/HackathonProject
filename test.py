import re
import nltk
import csv
from multiprocessing import cpu_count
from gensim.models import doc2vec
from gensim.models.word2vec import Word2Vec
from gensim.models.doc2vec import Doc2Vec
import pymorphy2

class Vector:
    def __init__(self):
        self.book_name = []
        self.book_desc = []
        self.book_desc_norm = []

    def pos(self,word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

    def parsi(self):
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

        #Создаем массив векторов описания
        with open("books.csv", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            for row in file_reader:
                for elem in range(len(row)):
                    words = row[elem].lower().split()
                    functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
                    s = [word for word in words if self.pos(word) not in functors_pos]
                    result = ""
                    for i in range(len(s)):
                        result += s[i]+" "
                    result = result.replace("то","")
                    result = re.sub('[^a-zA-ZА-я]', ' ', result)
                    result = result.replace("  ", " ")
                    result = result.replace("   ", " ")
                    result = result.replace("    ", " ")
                    result = result.replace("     ", " ")
                    result = result.replace("      ", " ")
                    if len(row[1].split()) > 13:
                        if elem == 0:
                            self.book_name.append(row[elem])
                        else:
                            self.book_desc_norm.append(row[elem])
                            self.book_desc.append(result)

    def similarity(self, text):
        d2v_model = Doc2Vec.load('d2v_Model')
        test_text = text
        test_text = re.sub('[^a-zA-ZА-я]', ' ', test_text)
        test_text = test_text.lower().split()
        inferred_vector = d2v_model.infer_vector(test_text)
        sims = d2v_model.dv.most_similar([inferred_vector], topn=10)
        for i in range(len(sims)):
            print("----------")
            print(self.book_name[sims[i][0]], end="\n")
            print(self.book_desc_norm[sims[i][0]], end="\n")
            print("----------")
        return sims

# #Для обучения модели нам нужен список целевых документов
# def tagged_document(list_of_ListOfWords):
#     for x, ListOfWords in enumerate(list_of_ListOfWords):
#         yield doc2vec.TaggedDocument(ListOfWords, [x])
#
#
# #тренировочные данные
# data_train = list(tagged_document(book_desc))
# d2v_model = doc2vec.Doc2Vec(vector_size=40, min_count=2, epochs=30)
# #расширить словарный запас
# d2v_model.build_vocab(data_train)
#
# #Обучение модели Doc2Vec
# d2v_model.train(data_train, total_examples=d2v_model.corpus_count, epochs=d2v_model.epochs)
#
# # Анализ выходных данных
# analyze = d2v_model.infer_vector(['нож', 'студент', 'топор', 'старуха'])
# #Запись модели
# d2v_model.save('d2v_Model')









