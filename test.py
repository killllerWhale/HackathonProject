import re
import csv
import urllib.request
from gensim.models.doc2vec import Doc2Vec
import pymorphy2

class Vector:
    def __init__(self):
        logo = urllib.request.urlopen("https://drive.google.com/u/0/uc?id=1bhwREIVAu9pqnP-jnOIbHmuJb99hanR_&export=download").read()
        f = open("d2v_Model_new", "wb")
        f.write(logo)
        f.close()
        self.book_name = []
        self.book_desc = []
        self.book_desc_norm = []

    def pos(self,word, morth=pymorphy2.MorphAnalyzer()):
        return morth.parse(word)[0].tag.POS

    def parsi(self):
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
        d2v_model = Doc2Vec.load('d2v_Model_new')
        test_text = text.lower().split()
        functors_pos = {'INTJ', 'PRCL', 'CONJ', 'PREP'}
        s = [word for word in test_text if self.pos(word) not in functors_pos]
        result = ""
        for i in range(len(s)):
            result += s[i] + " "
        result = re.sub('[^a-zA-ZА-я]', ' ', result)
        result = result.replace("  ", " ")
        result = result.replace("   ", " ")
        result = result.replace("    ", " ")
        result = result.replace("     ", " ")
        result = result.replace("      ", " ")
        result = result.lower().split()
        inferred_vector = d2v_model.infer_vector(result)
        sims = d2v_model.dv.most_similar([inferred_vector], topn=10)
        return sims

