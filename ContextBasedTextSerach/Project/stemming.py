import nltk
from nltk import FreqDist
from tempfile import TemporaryFile
from xlwt import Workbook
from nltk.corpus import stopwords
book = Workbook(encoding="utf-8")
sheet1 = book.add_sheet('Sheet 1')
sheet1.col(0).width = 10000
List=nltk.corpus.gutenberg.fileids()
L=[]
actual=[]
row=0
porter = nltk.PorterStemmer()
for l in List :
    sheet1.write(row,0,l)
    L=nltk.corpus.gutenberg.words(l)
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in L if w not in stopwords]
    actaul=[w for w in content if len(w)>1]
    stem=[porter.stem(t) for t in actual]
    col=1
    for m in stem[:255]:
        sheet1.write(row,col,m)
        col+=1
    row+=1
book.save('stem.xls')
book.save(TemporaryFile())
