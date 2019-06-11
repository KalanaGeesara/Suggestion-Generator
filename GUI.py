from tkinter import *

from tkinter import messagebox

from pyfasttext import FastText

from itertools import permutations

import hashlib

import datetime


#
# def hashing_tagged_copus():  # hash tagging function for all the unique words in the tagged corpus
#     filepath = "tagged.txt"
#     a = {}
#     with open(filepath) as fp:
#         for line in fp:
#             x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
#             if (len(x) == 2):
#                 if x[0] not in a:
#                     a[x[0]] = 0
#                 else:
#                     a[x[0]] += 1
#     hashed_dic = {}
#
#     for i in a:
#         encoded_word = i.encode('utf-8')
#         hash_object = hashlib.sha512(encoded_word)  # hash each word in the dictionary
#         hex_dig = hash_object.hexdigest()
#         if type(a[i]) is int:
#             hashed_dic[hex_dig] = a[i]
#         else:
#             hashed_dic[hex_dig] = 0
#
#     return hashed_dic

def get_hash(word):
    encoded_word = word.encode('utf-8')
    hash_object = hashlib.sha512(encoded_word)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def hashing_tagged_copus():
    filepath = "hashed_dic"
    a = {}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = int(x[1])
    return a


def is_papili_missing_word(word1, word2):
    array = []
    for i in word2:
        array.append(i)
    for i in word1:
        if i in array:
            array.remove(i)
    if len(array) > 0:
        if array[0] == 'ු' or array[0] == 'ූ' or array[0] == '්' or array[0] == 'ා' or array[0] == 'ි' or array[0] == 'ී':
            return True
        else:
            return False
    else:
        return False


def show_entry_fields():  # Display box function
    print(suggestion_generator(e1.get()))
    msg = messagebox.showinfo("Hello_Python", suggestion_generator(e1.get()))


def call_counter(func):  # Part of the levenshtein minimum edit distance algorithm
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)

    helper.calls = 0
    helper.__name__ = func.__name__
    return helper


def memoize(func):
    mem = {}

    def memoizer(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in mem:
            mem[key] = func(*args, **kwargs)
        return mem[key]

    return memoizer


@call_counter
@memoize
def levenshtein(s, t):  # Minimum edit distance algorithm
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([levenshtein(s[:-1], t) + 1,
               levenshtein(s, t[:-1]) + 1,
               levenshtein(s[:-1], t[:-1]) + cost])
    return res


# print(levenshtein("ළකුණ", "ලකුණු"))
# print("The function was called " + str(levenshtein.calls) + " times!")


def nana_lala(word):  # function which generates permutations of a given word
    # Get all permutations of length 2 
    # and length 2
    all = ['න', 'ණ', 'ල', 'ළ', 'ශ', 'ෂ', 'ත', 'ථ', 'බ', 'භ']
    simple = ['න', 'ල', 'ශ', 'ත', 'බ']
    capital = ['ණ', 'ළ', 'ෂ', 'ථ', 'භ']
    indices = []
    word_lst = []
    permutated_words = [word]
    for i in word:  # put all the letters in the word to a list
        word_lst.append(i)
    for i in range(len(word_lst)):
        if word_lst[i] in all:  # get the index numbers of the Nana Lala letters of that particular word
            indices.append(i)
    final = []
    for i in range(1, len(indices) + 1):

        perm = permutations(indices, i)  # Generate the permutations

        # Print the obtained permutations
        for i in list(perm):
            lst = []
            for j in i:
                lst.append(j)
            lst.sort()
            if lst not in final:
                final.append(lst)
    for i in final:
        for j in range(len(i)):
            if word_lst[i[j]] == 'න':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ණ'
            if word_lst[i[j]] == 'ණ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'න'
            if word_lst[i[j]] == 'ල':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ළ'
            if word_lst[i[j]] == 'ළ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ල'
            if word_lst[i[j]] == 'ශ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ෂ'
            if word_lst[i[j]] == 'ෂ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ශ'
            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'භ'
            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'බ'
            if word_lst[i[j]] == 'ත':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ථ'
            if word_lst[i[j]] == 'ථ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'ත'
            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'භ'
            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                per_word[i[j]] = 'බ'
        concat = ''
        for k in per_word:
            concat += k
        permutated_words.append(concat)
    return permutated_words


model = FastText('sinhala_all2.bin')

hashed_dic = hashing_tagged_copus()


def suggestion_generator(sinhala_word):
    # model = FastText('sinhala_all2.bin')
    a = datetime.datetime.now()
    #    print(model.similarity('බල්ල', 'බල්ලා'))
    sin_word = sinhala_word
    permutated_sin_word = nana_lala(sin_word)

    words = model.nearest_neighbors(sin_word, k=20000)

    suggested_words = []
    for i in words:
        minimum_edit_distance = levenshtein(i[0], sin_word)
        if minimum_edit_distance <= 1 or (
                get_hash(i[0]) in hashed_dic and minimum_edit_distance == 2 and hashed_dic[get_hash(i[0])] > 1500):
            # copy_suggested_words.remove(i)
            suggested_words.append(i[0])
    copy_suggested_words = suggested_words.copy()
    priority_suggested_words = {}
    for i in suggested_words:
        if i in permutated_sin_word:
            hex_dig = get_hash(i)
            if hex_dig not in hashed_dic:
                copy_suggested_words.remove(i)
            else:
                copy_suggested_words.remove(i)
                priority_suggested_words[i] = hashed_dic[hex_dig]  # Nana Lala error word are in the priority words list

    frequency_dic = {}
    for i in copy_suggested_words:
        hex_dig = get_hash(i)
        if hex_dig not in hashed_dic:
            copy_suggested_words.remove(i)
        else:
            frequency_dic[i] = hashed_dic[hex_dig]

    sorted_frequency_dic = sorted(frequency_dic.items(), key=lambda kv: kv[1])
    v1 = sorted_frequency_dic[::-1]
    v1_copy = v1.copy()
    # convertWordToArray = []
    # print(sin_word)
    # print(sinhala_word)
    # for i in sin_word:
    #     convertWordToArray.append(i)
    # print(convertWordToArray)
    ispiliWords = {}
    for i in v1_copy:
        if is_papili_missing_word(sin_word, i[0]):
            ispiliWords[i[0]] = i[1]
            v1.remove(i)

    v3 = sorted(ispiliWords.items(), key=lambda kv: kv[1])

    for i in v3:
        v1.insert(0, i)
    # print(v1)

    sorted_frequency_dic = sorted(priority_suggested_words.items(), key=lambda kv: kv[1])
    v2 = sorted_frequency_dic[::-1]

    max = 0
    max_word = ''
    # print(permutated_sin_word)
    for i in permutated_sin_word:
        hex_dig = get_hash(i)
        if hex_dig in hashed_dic:
            if hashed_dic[hex_dig] > max:
                max = hashed_dic[hex_dig]
                max_word = i
    # print(max)
    # print(v2)
    if len(permutated_sin_word) == 1:
        if len(v2) > 1 and v2[0][1] <= max:
            v2.insert(0, max_word)
    elif len(permutated_sin_word) > 1 and max != 0:
        if (max_word, max) not in v2 and (max_word, max) not in v1:
            v2.insert(0, (max_word, max))

    v = v2 + v1
    print(v1)
    b = datetime.datetime.now()
    print(b - a)
    return v[:5]


# print(suggestion_generator('කකුළ'))

master = Tk()
Label(master, text="වචනය").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()
