from PyQt4 import Qt,QtCore,QtGui
import nltk
import sys
#try:
import btpgui
import glob
import os
from collections import Counter
import math
from nltk import PorterStemmer
import time

class ApplicationWindow(QtGui.QMainWindow,btpgui.Ui_MainWindow):
    def __init__(self):
        super(ApplicationWindow,self).__init__()
        self.setupUi(self)
        self._connectSlots()
        self.documents = []
        self.SPECIAL_CHARACTERS = ['.', '?', ',', '!', "'s", "'"]
        self.posting_list = {}
        self.document_length = {}
        self.vocabulary = set([])
        self.idf = {}
        self.K1 = 1.5
        self.B = 0.75
        self.score = {}


        # List all files
        for file in glob.glob("*.txt"):
            self.documents.append(file)
            self.posting_list[file] = {}
            self.score[file] = 0
        self.documents.remove('inverted-index.txt')
        self.posting_list.pop('inverted-index.txt')
        self.score.pop('inverted-index.txt')
        print('List of Documents:', self.documents)

         # Remove special characters
    def removeSpecialCharacters(self, string):
        for character in self.SPECIAL_CHARACTERS:
            if character in string:
                string = string.replace(character, '')
        return string
     # Stem a word
    def stem(self, word):
        return PorterStemmer().stem_word(word)

    def _connectSlots(self):
        QtCore.QObject.connect(self.click,QtCore.SIGNAL("clicked()"),self.getQuery)

    def getQuery(self):
        global doc
        queryText = self.input.toPlainText()
        print (queryText)
        query = self.removeSpecialCharacters(queryText)
        query = list(query.split())
        query = list(map(self.stem, query))
        print
        print('Your Query:', queryText)

        # Reading already existing inverted index
        with open ('inverted-index.txt', "r") as f:
            test = f.read().replace('\n', ' ')
        if test == "":
            test = []
        else:
            test = test[:-2]
            test = test.split(';')
        self.posting_list = {}

        for x in test:
            temp = x.split(':')
            doc_name = temp[0].strip()
            doc_index = temp[1].strip()
            self.posting_list[doc_name] = {}
            temp2 = doc_index.split(',')
            for y in temp2:
                y = y.strip().split('=')
                y[0] = y[0].strip()
                y[1] = int(y[1])
                self.posting_list[doc_name][y[0]] = y[1]


        docs_indexed = self.posting_list.keys()
        print('docs_indexed:', docs_indexed)
        print
        docs_remaining = set(self.documents).difference(set(docs_indexed))
        print('docs_remaining:', docs_remaining)
        docs_delete = set(docs_indexed).difference(set(self.documents))
        print('docs_delete:', docs_delete)
        for doc in docs_delete:
            self.posting_list.pop(doc)
        # Adding words in vocabulary and document length of the documents indexed already
        for doc in self.posting_list:
            self.document_length[doc] = sum(self.posting_list[doc].values())
            self.vocabulary.update(set(self.posting_list[doc].keys()))


        # Creating inverted index according to the query
        for aDocument in docs_remaining:
            # Read the document
            with open (aDocument, "r") as f:
                test = f.read().replace('\n', ' ')
            # Remove special characters and convert into lowercase
            test = self.removeSpecialCharacters(test).lower()
            # Make string into list
            test = test.split()
            # Stem
            test = map(self.stem, test)
            test = Counter(test).most_common()
            test = dict((x, y) for x, y in test)
            self.document_length[aDocument] = sum(test.values())
            # Adding words into vocabulary
            self.vocabulary.update(set(test.keys()))
            # Creating inverted index for the document
            self.posting_list[aDocument] = {}
            for term in test:
                self.posting_list[aDocument][term] = test[term]


        # Adding respective remaining words to all docs inverted index
        for doc in self.posting_list:
            for term in self.vocabulary:
                if term not in self.posting_list[doc]:
                    self.posting_list[doc][term] = 0


        print('Document Length:', self.document_length)
        print('Posting List:')
        for doc in self.posting_list:
            print(doc,len(self.posting_list[doc].keys()))

        # Calculate IDF
        for term in query:
            n = self.numDocuments(term)
            if n == 0:
                self.idf[term] = 0.0
            else:
                self.idf[term] = math.log(len(self.documents) / float(n))
                #idf[term] = math.log((len(documents) - n + 0.5) / (n + 0.5))

        print('IDF:', self.idf)
        #for keys in self.idf.keys():
           # self.idfText.appendPlainText(str(self.idf.get(keys)))

        # Calculate Score
        avgdl = sum(self.document_length.values()) / float(len(self.document_length))
        for doc in self.documents:
            for term in query:
                if term in self.posting_list[doc]:
                    self.score[doc] += (self.idf[term])* (((self.posting_list[doc][term]) * (self.K1 + 1)) / ((self.posting_list[doc][term]) + (self.K1 * (1 - self.B + (self.B * (self.document_length[doc] / avgdl))))))
                else:
                    self.score[doc] += 0.0
        print ('Score:',self.score)
        #for scoreKeys in self.score.keys():
            #self.scoreText.appendPlainText(str(self.score.get(scoreKeys)))

        for doc in [k for k in sorted(self.score, key=self.score.get, reverse=True)]:
            # print (doc)
            outputText = "<a href=doc>" + doc +"</a>"
            #t = Qt.QMouseEvent()
            #t.ActionAdded(self.callSelectedTextPopUp)
            #self.output.mousePressEvent(t)
            #self.output.mouseDoubleClickEvent(self.callSelectedTextPopUp)
            #self.output.selectionChanged(self.callSelectedTextPopUp)
            #self.output.appendPlainText(outputText)
            self.output.appendHtml(outputText)

        # Writing back the new inverted index in the file
        if len(docs_remaining) != 0:
            f = open('inverted-index.txt', 'w')
            for temp in self.posting_list:
                string = ""
                string = string + temp + ': '
                for temp2 in self.posting_list[temp]:
                    string = string + temp2 + ' = ' + str(self.posting_list[temp][temp2]) + ', '
                string = string[:-2] + ';\n'
                f.write(string)
            f.close()


    def callSelectedTextPopUp(self):
        print ("Selection Text Changed")
    # numDocuments
    def numDocuments(self,term):
        count = 0
        for doc in self.posting_list:
            if term in self.posting_list[doc]:
                if self.posting_list[doc][term] > 0:
                    # print ("Hello")
                    count += 1
                # print("hello")
        print(count)

        return count





if __name__=='__main__':
    app=Qt.QApplication(sys.argv)
    guiapp=ApplicationWindow()
    guiapp.show()
    app.exec_()