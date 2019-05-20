from tkinter import *

from tkinter import messagebox

from pyfasttext import FastText

from itertools import permutations

def show_entry_fields():
   print(suggestion_generator(e1.get()))
   msg = messagebox.showinfo( "Hello Python", suggestion_generator(e1.get()))
##   label.pack()
##   e1.delete(0,END)

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


def suggestion_generator(sinhala_word):  
    model = FastText('sinhala_all.bin')

    #print(model.similarity('බල්ල', 'බල්ලා'))
    sin_word = sinhala_word
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
    
    return copy_suggested_words[:5]

master = Tk()
Label(master, text="First Name").grid(row=0)

e1 = Entry(master)
##e1.insert(10,"Miller")

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
