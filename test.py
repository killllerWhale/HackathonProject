import numpy as np
from scipy import spatial
from gensim.models import Word2Vec
import re
import nltk

import csv
model_string = ""
with open("books.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Считывание данных из CSV файла
    for row in file_reader:
        for elem in row:
            model_string += elem + " "
processed_article = model_string.lower()
processed_article = re.sub('[^a-zA-Z]', ' ',processed_article )
processed_article = re.sub(r'\s+', ' ', processed_article)
# Preparing the dataset
all_sentences = nltk.sent_tokenize(processed_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]
word2vec = Word2Vec(all_words)
vocabulary = word2vec.wv.key_to_index
print(vocabulary)

#print(model_string)

# index2word_set = set(model.wv.index2word)
#
# def avg_feature_vector(sentence, model, num_features, index2word_set):
#     words = sentence.split()
#     feature_vec = np.zeros((num_features, ), dtype='float32')
#     n_words = 0
#     for word in words:
#         if word in index2word_set:
#             n_words += 1
#             feature_vec = np.add(feature_vec, model[word])
#     if (n_words > 0):
#         feature_vec = np.divide(feature_vec, n_words)
#     return feature_vec
#
# s1_afv = avg_feature_vector('Серия романов о волшебнике Гарри Поттер', model=model, num_features=300, index2word_set=index2word_set)
# s2_afv = avg_feature_vector('Серия романов, написанная британской писательницей Дж. К. Роулинг. Книги представляют собой хронику приключений юного волшебника Гарри Поттера, а также его друзей Рона Уизли и Гермионы Грейнджер, обучающихся в школе чародейства и волшебства Хогвартс. Основной сюжет посвящён противостоянию Гарри и тёмного волшебника по имени лорд Волан-де-Морт, в чьи цели входит обретение бессмертия и порабощение магического мира.', model=model, num_features=300, index2word_set=index2word_set)
# sim = 1 - spatial.distance.cosine(s1_afv, s2_afv)
# print(sim)