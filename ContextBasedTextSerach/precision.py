import os
import glob
import math
import nltk.data
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from tempfile import TemporaryFile
from xlwt import Workbook
import xlrd
documents = []
book=Workbook(encoding="utf-8")
sheet1=book.add_sheet('Sheet1',cell_overwrite_ok=True)
sheet2=book.add_sheet('Sheet2',cell_overwrite_ok=True)

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
list_of_files = glob.glob("*.txt")
documents.append(list_of_files)
n = (len(list_of_files))
print(n,"check1")
s=[]
p=[]
r=[]
t=[]
q=[]
a=[]
res=[0,0,0,0]
print(res[1],"check2")
cat=["2","2","3","4","1","1"]
#print(cat[2])
num=0
for fileName in list_of_files:
    s=[]
    p=[]
    r=[]
    t=[]
    q=[]
    a=[]
    fin=open(fileName,"r")
    data=fin.read()
    print(fileName,"check3")
    print(data)
    #inp=input("enter your opinion:")
    inp=input("press 1 for sports 2 for education 3 for entertainment 4 for politics 5 for business")
    print(inp)
    for line in data.split('\n'):
        #print(line)
        r.append(line)
        #print(type(s))
        s.append(word_tokenize(line))
        #print(word_tokenize(line))
        fin.close() #closes file
#print(s) 
    for i in range(len(s)):
        r.append(i)
#print(r)

    t = word_tokenize(str(r))
    print(t)
    p = nltk.corpus.stopwords.words('english')
    #print(p)
    for w in t:
        if w not in p:
            q.append(w)


    #for i in q:
     #   stemmer = PorterStemmer()
      #  if(len(stemmer.stem(i))>4):
       #     a.append(stemmer.stem(i))
        #print(stemmer.stem(i)

    word_set = set(a)
    s=(len(word_set))
    freq = {}
    prob = {}
    #i = 1 

    CAT=['input']

    row=0
    col=1
    for m in CAT[:255]:
        sheet1.write(row,col,m)
        col+=1
   
    row=1
    col=1
    for word in word_set:
        sheet1.write(row,0,word)
        freq[word] = a.count(word)
        fq=freq[word]
        #print(fq)
        prob[word] =(a.count(word)/float(len(a)))
        pb=prob[word]
        sheet1.write(row,col,pb)
        row+=1

    print("***********probability of document in particular class*******")
    #print(i)
    book.save('precision.xls')
    book.save(TemporaryFile())

    file_location="precision.xls"
    workbook=xlrd.open_workbook(file_location)
    Sheet=workbook.sheet_by_index(0)
    R=Sheet.nrows
    print(R)
    file_location="precision.xls"
    workbook1=xlrd.open_workbook(file_location)
    Sheet1=workbook1.sheet_by_index(0)
    Ri=Sheet1.nrows
    print(Ri)
#for word in word_set:
    psport= 1.0
    ped= 1.0
    ppol= 1.0
    pbusi= 1.0
    penter= 1.0                       
    for i in range(Ri-1):
        for j in range(R):
                word=Sheet1.cell_value(i,0)
                val=Sheet.cell_value(j,0)
                #print(val)
                #print(str(word))
                if(str(word)==val):
                        a1=Sheet.cell_value(j+1,1)
                        #print(type(a1))
                        #c=float(a1)
                        #a1=a1.strip()
                        #c=float(a1)
                        #print((int(c)*1000)/1000)
                        a2=Sheet.cell_value(j+1,2)
                        a3=Sheet.cell_value(j+1,3)
                        a4=Sheet.cell_value(j+1,4)
                        a5=Sheet.cell_value(j+1,5)
                        v1=Sheet.cell_value(j,0)
                        #print(a)
                        #print(v1)
                        b=Sheet1.cell_value(i+1,1)
                        v2=Sheet1.cell_value(i,0)
                        #print(b)
                        #print(v2)
                        #print(i+1)
                         
                        if(a1==""):
                                a1=1.0
                        if(a2==""):
                                a2=1.0
                        if(a3==""):
                                a3=1.0
                        if(a4==""):
                                a4=1.0
                        if(a5==""):
                                a5=1.0
                        if(b==""):
                                b=1.0

                        c=float(a1)
                        #a1=a1.strip()
                        q1=(int(c*10000000000000)/10000000000000)
                        a11= "%.10f" %q1
                        #print(a11)

                        c1=float(a2)
                        #a1=a1.strip()
                        q2=(int(c1*10000000000000)/10000000000000)
                        a12="%.10f" %q2

                        c2=float(a3)
                        #a1=a1.strip()
                        q3=(int(c2*10000000000000)/10000000000000)
                        a13="%.10f" %q3

                        c3=float(a4)
                        #a1=a1.strip()
                        q4=(int(c3*10000000000000)/10000000000000)
                        a14="%.10f" %q4

                        c4=float(a5)
                        #a1=a1.strip()
                        q5=(int(c4*10000000000000)/10000000000000)
                        a15="%.10f" %q5

                        #print("probability of new document in sports")
                        
                        
                        psport=abs(math.log(float(a11)*psport))
                        #psport1="%.15f" %psport
                        #print(psport)

                        #print("probability of new document in education")

                        
                        ped=abs(math.log(float(a12)*ped))
                        #print(ped)

                        
                        #print("probability of new document in politics")

                        
                        ppol=abs(math.log(float(a13)*ppol))
                        #print(ppol)

                        
                        #print("probability of new document in business")

                        pbusi=abs(math.log(float(a14)*pbusi))
                        #print(pbusi)

                        
                        #print("probability of new document in entertainment")

                        """print(a15)
                        penter=abs(math.log(float(a15)*penter))
                        print(penter)"""
    print("////////////////////category///////////////////////////////")
    print(psport)
    print(ped)
    print(ppol)
    print(pbusi)
#print(penter)

    t= [psport,ped,ppol,pbusi,penter]
    m=max(t,key=float)
    print(m)

    if(m==psport):
        print("document belongs to SPORTS CATEGORY")
        m=1
    if(m==ped):
        print("document belongs to EDUCATION CATEGORY")
        m=2
    if(m==ppol):
        print("document belongs to POLTICS CATEGORY")
        m=3
    if(m==pbusi):
        print("document belongs to BUSINESS CATEGORY")
        m=4
    if(m==penter):
        print("document belongs to ENTERTAINMENT CATEGORY")
        m=5

    if((m==cat[num])):
        if((cat[num]==inp)):
            #print("selected and correct")
            res[0]=res[0]+1
        else:
            res[1]=res[1]+1
    if(m!=cat[num]):
        if((cat[num]==inp)):
            #print("selected and correct")
            res[2]=res[2]+1
        else:
            res[3]=res[3]+1
        
    num=num+1

print(res)

