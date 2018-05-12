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
row=0 
for l in List :
    sheet1.write(row,0,l)
    L=nltk.corpus.gutenberg.words(l)
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in L if w not in stopwords]
    actaul=[w for w in content if len(w)>1]
    col=1
    for m in actaul[:255]:
        sheet1.write(row,col,m)
        col+=1
    row+=1
book.save('simple.xls')
book.save(TemporaryFile())
