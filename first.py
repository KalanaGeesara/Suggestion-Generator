##import fasttext
##import gensim
##model = gensim.models.KeyedVectors.load_word2vec_format('model.vec')
##similar = model.most_similar(positive=['ඛණ'],topn=10)
##print(similar)

##from gensim.models.wrappers import FastText
##
##model = FastText.load_fasttext_format('model')
##
##print(model.most_similar(positive=['ඛණ'],topn=10))
##


from pyfasttext import FastText

from itertools import permutations

def NanaLala(word): 
    # Get all permutations of length 2 
    # and length 2
    all = ['න','ණ','ල','ළ']
    simple = ['න','ල']
    capital = ['ණ','ළ']
    indices =[]
    word_lst = []
    permutated_words=[]
    permutated_words.append(word)
    for i in word:
        word_lst.append(i)
    for i in range(len(word_lst)):
        if word_lst[i] in all:
            indices.append(i)
    final=[]
    for i in range(1,len(indices)+1):
            
        perm = permutations(indices, i) 
  
    # Print the obtained permutations
        for i in list(perm):
            lst=[]
            for j in i:
                lst.append(j)
            lst.sort()
            if lst not in final:
                final.append(lst)
    
    for i in final:
        for j in i:
            if word_lst[j]=='න':
                if len(i)<=1:
                    per_word = word_lst.copy()
                per_word[j] = 'ණ'
            if word_lst[j]=='ණ':
                if len(i)<=1:
                    per_word = word_lst.copy()
                per_word[j] = 'න'
            if word_lst[j]=='ල':
                if len(i)<=1:
                    per_word = word_lst.copy()
                per_word[j] = 'ළ'
            if word_lst[j]=='ළ':
                if len(i)<=1:
                    per_word = word_lst.copy()
                per_word[j] = 'ල'
        concat = ''
        for k in per_word:
            concat+=k
        permutated_words.append(concat)          
    return permutated_words


  
model = FastText('sinhala_all.bin')

#print(model.similarity('බල්ල', 'බල්ලා'))
sin_word = 'බළ්ළාට'
permutated_sin_word = NanaLala(sin_word)
words = model.nearest_neighbors(sin_word, k=10000)
suggested_words = []
for i in words:
    suggested_words.append(i[0])
copy_suggested_words = suggested_words.copy()
for i in suggested_words:
    if i in permutated_sin_word:
        copy_suggested_words.remove(i)
        copy_suggested_words.insert(0,i)
    
print(copy_suggested_words[:5])


