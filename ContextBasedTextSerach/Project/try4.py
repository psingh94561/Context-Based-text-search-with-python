import nltk
from nltk import FreqDist
import math
from collections import Counter

List=nltk.corpus.gutenberg.fileids()
vocab=nltk.corpus.gutenberg.words(List)
L=[]
t=[]
for l in List:
        L.append(nltk.corpus.gutenberg.words(l))
#Input=raw_input("Enter the query:")
#text=nltk.word_tokenize(Input)
#Finput=FreqDist(text)

def build_vector(iterable1, iterable2):
    counter1 = Counter(iterable1)
    counter2 = Counter(iterable2)
    all_items = set(counter1.keys()).union(set(counter2.keys()))
    vector1 = [counter1[k] for k in all_items]
    vector2 = [counter2[k] for k in all_items]
    return vector1, vector2

def cosim(v1, v2):
    dot_product = sum(n1 * n2 for n1, n2 in zip(v1, v2) )
    magnitude1 = math.sqrt(sum(n ** 2 for n in v1))
    magnitude2 = math.sqrt(sum(n ** 2 for n in v2))
    return dot_product / (magnitude1 * magnitude2)

for p in L:
        l1 =L[0]
        l2=p
        v1, v2 = build_vector(l1, l2)
        print(cosim(v1, v2))
