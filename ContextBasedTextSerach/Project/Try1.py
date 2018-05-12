import nltk
import re ,math
from nltk import FreqDist
lisT=nltk.corpus.gutenberg.fileids()
Vocab=nltk.corpus.gutenberg.words(lisT)
Input=raw_input("Input Your Qurey ")
text = nltk.word_tokenize(Input)
Finput=FreqDist(text)
L=[]
S=[]
a,b,c=0,0,0 
for l in lisT:
    L.append(nltk.corpus.gutenberg.words(l))
for s in L:
    S.append(FreqDist(s))
for t in S :
    for v in Vocab:
        a=a+(S[0][v]*t[v])
        b=b+(S[0][v]*S[0][v])
        c=c+(t[v]*t[v])
    b=math.sqrt(b)
    c=math.sqrt(c)
    cos=a/(b*c)
    print a , b ,c ,cos
    print len(t)
x=121
print math.sqrt(36)
print math.sqrt(x)
    
