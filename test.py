import re
import nltk
import csv
from multiprocessing import cpu_count
from gensim.models.word2vec import Word2Vec
import gensim
import gensim.downloader as api
from gensim.models import doc2vec


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
def tagged_document(list_of_ListOfWords):
    for x, ListOfWords in enumerate(list_of_ListOfWords):
        yield doc2vec.TaggedDocument(ListOfWords, [x])


# тренировочные данные
data_train = list(tagged_document(book_desc))

# вывести обученный набор данных
print(data_train[:1])

#print(book_desc)
# print(book_name)




