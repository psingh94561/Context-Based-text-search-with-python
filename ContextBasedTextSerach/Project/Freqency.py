import nltk
from nltk import FreqDist
from tempfile import TemporaryFile
from xlwt import Workbook
from nltk.corpus import stopwords
book = Workbook(encoding="utf-8")
sheet1 = book.add_sheet('Sheet 1')
List=nltk.corpus.gutenberg.fileids()
W=set(nltk.corpus.gutenberg.words(List))
stopwords = nltk.corpus.stopwords.words('english')
C = [w for w in W if w not in stopwords]
Vocab=[w for w in C if len(w)>1]
row=1
for v in Vocab[:65535]:
    sheet1.write(row,0,v)
    row+=1
col=1
for l in List :
    sheet1.write(0,col,l)
    col+=1
L=[]
F=[]
for l in List:
    L.append(nltk.corpus.gutenberg.words(l))
for s in L:
    F.append(FreqDist(s))
r=1
for m in Vocab[:65535]:
    c=1
    for n in range(0,len(List)):
        sheet1.write(r,c,F[n][m])
        c+=1
    r+=1
book.save('FreqDist.xls')
book.save(TemporaryFile())
