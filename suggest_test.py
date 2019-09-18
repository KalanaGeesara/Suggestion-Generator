from tkinter import *

from tkinter import messagebox

from pyfasttext import FastText

from itertools import permutations

import hashlib

import datetime

import math


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
#     return hashed_dic/home/kalana

def get_hash(word):
    encoded_word = word.encode('utf-8')
    hash_object = hashlib.sha512(encoded_word)
    hex_dig = hash_object.hexdigest()
    return hex_dig


def hashing_tagged_copus():
    filepath = "hashed_dic2"
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
        if array[0] == 'ු' or array[0] == 'ූ' or array[0] == '්' or array[0] == 'ා' or array[0] == 'ි' or array[0] == 'ී' or array[0] == 'ී' or array[0] == 'ෑ' or array[0] == 'ැ':
            return True
        else:
            return False
    else:
        return False


def is_joiner_missing_word(word1, word2):
    array = []
    for i in word2:
        array.append(i)
    for i in word1:
        if i in array:
            array.remove(i)

    if len(array) > 0:
        if array[0] == '\u200d':
            return True
        else:
            return False
    else:
        return False


def split_check(words, word):
    first_word =[]
    last_word = []
    space_suggestion = []
    for i in words:
        if i[0] != '' and word != '' and i[0][0] != '' and i[0][0] == word[0] and i[0] in word:
            if get_hash(i[0]) in hashed_dic:
                first_word.append(i[0])
        if i[0] != '' and word != '' and i[0][-1] != '' and i[0][-1] == word[-1] and i[0] in word:
            if get_hash(i[0]) in hashed_dic:
                last_word.append(i[0])
    for i in first_word:
        for j in last_word:
            if i+j == word and get_hash(word) in hashed_dic:
                s = i + ' ' + j
                space_suggestion.append(s)
    return space_suggestion


def get_modified_input_word(word):
    new_sin_word = word
    if '්යා' in word and 'ර්යා' not in word:
        new_sin_word = new_sin_word.replace('්යා', '්‍යා')
    if '්ය' in word and 'ර්ය' not in word:
        new_sin_word = new_sin_word.replace('්ය', '්‍ය')

    if 'බ්රිී' in word:
        new_sin_word = new_sin_word.replace('බ්රිී', 'බ්‍රි')
    if 'ක්රි' in word:
        new_sin_word = new_sin_word.replace('ක්රි', 'ක්‍රි')
    if 'ප්රි' in word:
        new_sin_word = new_sin_word.replace('ප්රි', 'ප්‍රි')
    if 'ග්රි' in word:
        new_sin_word = new_sin_word.replace('ග්රි', 'ග්‍රි')
    if 'ද්රි' in word:
        new_sin_word = new_sin_word.replace('ද්රි', 'ද්‍රි')

    if 'බ්රී' in word:
        new_sin_word = new_sin_word.replace('බ්රී', 'බ්‍රී')
    if 'ක්රී' in word:
        new_sin_word = new_sin_word.replace('ක්රී', 'ක්‍රී')
    if 'ප්රී' in word:
        new_sin_word = new_sin_word.replace('ප්රී', 'ප්‍රී')
    if 'ග්රී' in word:
        new_sin_word = new_sin_word.replace('ග්රී', 'ග්‍රී')
    if 'ද්රී' in word:
        new_sin_word = new_sin_word.replace('ද්රී', 'ද්‍රී')

    if 'බ්ර' in word:
        new_sin_word = new_sin_word.replace('බ්ර', 'බ්‍ර')
    if 'ප්ර' in word:
        new_sin_word = new_sin_word.replace('ප්ර', 'ප්‍ර')
    if 'ක්ර' in word:
        new_sin_word = new_sin_word.replace('ක්ර', 'ක්‍ර')
    if 'ග්ර' in word:
        new_sin_word = new_sin_word.replace('ග්ර', 'ග්‍ර')
    if 'ද්ර' in word:
        new_sin_word = new_sin_word.replace('ද්ර', 'ද්‍ර')

    return new_sin_word


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

def get_permutations(word, changed_letters):
    all = changed_letters
    indices = []
    word_lst = []
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
    return word_lst, final


def get_Bindu_words(word):
    all = ['න', 'ං']
    permutated_words = []
    word_lst, final = get_permutations(word, all)
    print(word_lst)
    print(final)
    for i in final:
        per_word = ['']
        inside_once = False
        for j in range(len(i)):
            print(i[j])
            print(len(word_lst))
            if word_lst[i[j]] == 'න' and i[j] < len(word_lst)-2 and word_lst[i[j]+1] == '්':
                if inside_once == False:
                    per_word = word_lst.copy()
                    inside_once = True
                print("LLLMMMM")
                per_word[i[j]] = 'ං'
                per_word[i[j]+1] = ''

        concat = ''
        for k in per_word:
            concat += k
        hash_dig = get_hash(concat)
        if (hash_dig in hashed_dic) and (concat not in permutated_words):
            permutated_words.append(concat)
    return permutated_words
            # if word_lst[i[j]] == 'ං':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #     per_word[i[j]] = 'න'
            #     per_word[i[j] + 1] = '්'


def nana_lala(word):  # function which generates permutations of a given word
    # Get all permutations of length 2
    # and length 2
    all = ['න', 'ණ', 'ල', 'ළ', 'ශ', 'ෂ', 'ත', 'ථ', 'බ', 'භ', 'ද', 'ධ', 'ග', 'ඳු', 'දු', 'ු', 'ූ', 'ට', 'ඨ', 'ච', 'ඡ', 'ජ']
    # simple = ['න', 'ල', 'ශ', 'ත', 'බ', 'ද']
    # capital = ['ණ', 'ළ', 'ෂ', 'ථ', 'භ', 'ධ']
    # indices = []
    # word_lst = []
    permutated_words = []
    # for i in word:  # put all the letters in the word to a list
    #     word_lst.append(i)
    # for i in range(len(word_lst)):
    #     if word_lst[i] in all:  # get the index numbers of the Nana Lala letters of that particular word
    #         indices.append(i)
    # final = []
    # for i in range(1, len(indices) + 1):
    #
    #     perm = permutations(indices, i)  # Generate the permutations
    #
    #     # Print the obtained permutations
    #     for i in list(perm):
    #         lst = []
    #         for j in i:
    #             lst.append(j)
    #         lst.sort()
    #         if lst not in final:
    #             final.append(lst)
    word_lst, final = get_permutations(word, all)
    for i in final:
        per_word = ['']
        for j in range(len(i)):
            dha_word = False
            if word_lst[i[j]] == 'න':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ණ'
                per_word2[i[j]] = 'ණ'

            if word_lst[i[j]] == 'ණ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'න'
                per_word2[i[j]] = 'න'

            if word_lst[i[j]] == 'ල':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ළ'
                per_word2[i[j]] = 'ළ'

            if word_lst[i[j]] == 'ළ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ල'
                per_word2[i[j]] = 'ල'

            if word_lst[i[j]] == 'ශ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ෂ'
                per_word2[i[j]] = 'ස'
                dha_word = True

            if word_lst[i[j]] == 'ෂ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'
                per_word2[i[j]] = 'ස'
                dha_word = True

            if word_lst[i[j]] == 'ස':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'
                per_word2[i[j]] = 'ෂ'
                dha_word = True

            if word_lst[i[j]] == 'ත':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ථ'
                per_word2[i[j]] = 'ථ'

            if word_lst[i[j]] == 'ථ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ත'
                per_word2[i[j]] = 'ත'

            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'භ'
                per_word2[i[j]] = 'භ'

            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'බ'
                per_word2[i[j]] = 'බ'

            if word_lst[i[j]] == 'ද':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ධ'
                per_word2[i[j]] = 'ඳ'
                dha_word = True

            if word_lst[i[j]] == 'ධ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ද'
                per_word2[i[j]] = 'ඳ'
                dha_word = True

            if word_lst[i[j]] == 'ග':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඟ'
                per_word2[i[j]] = 'ඟ'

            # if word_lst[i[j]] == 'දු':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #         per_word2 = word_lst.copy()
            #     per_word[i[j]] = 'ඳු'
            #
            # if word_lst[i[j]] == 'ඳු':
            #     if j <= 0:
            #         per_word = word_lst.copy()
            #         per_word2 = word_lst.copy()
            #     per_word[i[j]] = 'දු'

            if word_lst[i[j]] == 'ු':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ූ'
                per_word2[i[j]] = 'ූ'

            if word_lst[i[j]] == 'ූ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ු'
                per_word2[i[j]] = 'ු'

            if word_lst[i[j]] == 'ට':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඨ'
                per_word2[i[j]] = 'ඨ'

            if word_lst[i[j]] == 'ඨ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ට'
                per_word2[i[j]] = 'ට'

            if word_lst[i[j]] == 'ඡ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ච'
                per_word2[i[j]] = 'ජ'
                dha_word = True

            if word_lst[i[j]] == 'ච':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'
                per_word2[i[j]] = 'ඡ'

            if word_lst[i[j]] == 'ජ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'
                per_word2[i[j]] = 'ඡ'

        concat = ''
        for k in per_word:
            concat += k
        hash_dig = get_hash(concat)
        if hash_dig in hashed_dic:
            permutated_words.append(concat)
        modified_concat = get_modified_input_word(concat)
        hash_dig = get_hash(modified_concat)
        if hash_dig in hashed_dic:
            permutated_words.append(modified_concat)
        if dha_word:
            concat2 = ''
            for k in per_word2:
                concat2 += k

            hash_dig = get_hash(concat2)
            if hash_dig in hashed_dic:
                permutated_words.append(concat2)
            modified_concat2 = get_modified_input_word(concat2)
            hash_dig = get_hash(modified_concat2)
            if hash_dig in hashed_dic:
                permutated_words.append(modified_concat2)

    print(permutated_words)
    print("JJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJJ")
    return permutated_words

x1 = datetime.datetime.now()
model = FastText('sinhala_cleared_model.bin')

# model = FastText('result/fil9.bin')
y1 = datetime.datetime.now()

print("TIMETIMETIME=======")
print(y1-x1)
hashed_dic = hashing_tagged_copus()

print(len(hashed_dic))
print(hashed_dic[get_hash('බාධා')])
print(hashed_dic[get_hash('විෂයය')])
def suggestion_generator(sinhala_word):
    # model = FastText('sinhala_all2.bin')
    a = datetime.datetime.now()
    #    print(model.similarity('බල්ල', 'බල්ලා'))
    user_sin_word = sinhala_word
    sin_word = get_modified_input_word(sinhala_word)

    permutated_nana_lala_sin_word = nana_lala(sin_word)
    permutated_bindu_sin_word = get_Bindu_words(sin_word)

    permutated_sin_word = permutated_nana_lala_sin_word + permutated_bindu_sin_word
    words = model.nearest_neighbors(sin_word, k=2000)
    minnnnn = []
    min1 = {}
    min2 = {}
    min3 = {}
    min_other = {}
    min = 1000000000
    max_frequency = 0
    # print(words)
    suggested_words = []
    space_suggestion = split_check(words, sin_word)
    final_dic = {}
    for i in words:
        punc = [',','.','/','?']
        punctuation_free_word = ''
        for k in i[0]:
            if k not in punc:
                punctuation_free_word += k

        if punctuation_free_word == 'ළඟයි':
            print("KKKKKKKKKKKKKKKKKKKKKKKKKK")

        if get_hash(punctuation_free_word) in hashed_dic:
            final_dic[punctuation_free_word] = i[1] * math.log(hashed_dic[get_hash(punctuation_free_word)]+1) #add or remove the log

            if punctuation_free_word in permutated_sin_word:
                final_dic[punctuation_free_word] *= 10**1.35

            if is_papili_missing_word(sin_word, punctuation_free_word):
                final_dic[punctuation_free_word] *= 10**1.3

            if is_joiner_missing_word(sin_word, punctuation_free_word):
                final_dic[punctuation_free_word] *= 10**1.12

            minimum_edit_distance = levenshtein(punctuation_free_word, sin_word)

            if punctuation_free_word in permutated_sin_word:
                print(final_dic[punctuation_free_word])
                final_dic[punctuation_free_word] /= 10*minimum_edit_distance
                print("LLLLLLLLLLLLLLLLLLLLLLLLLL")
                print(punctuation_free_word)
                print(hashed_dic[get_hash('ළඟයි')])
            else:
                final_dic[punctuation_free_word] /= 10**minimum_edit_distance


    sorted_final_dic = sorted(final_dic.items(), key=lambda kv: kv[1])[::-1]
    if 'බාදා' in final_dic:
        print("KKKKKKKKKKKKKKKKKKKKKKKKKKK")

    max_frequency = 0
    max_word = ''
    print(permutated_sin_word)
    for i in permutated_sin_word:
        hex_dig = get_hash(i)
        if hex_dig in hashed_dic:
            if hashed_dic[hex_dig] / 10 ** levenshtein(i, sin_word) > max_frequency:
                max_frequency = hashed_dic[hex_dig] / 10 ** levenshtein(i, sin_word)
                max_word = i

    if max_word != '' and max_word not in final_dic:
        sorted_final_dic.insert(0, (max_word, max_frequency))
    elif max_word != '' and max_word in final_dic and (max_word, final_dic[max_word]) not in sorted_final_dic[:5]:
        sorted_final_dic.insert(0, (max_word, max_frequency))

    return sorted_final_dic[:5]


# print(suggestion_generator('කකුළ'))
a1 = datetime.datetime.now()
filepath2 = "extracted_misspelled_news"
print("FFFFFFF")
b = {}
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        b[x[0]] = suggestion_generator(x[0])
print(b)

f = open('suggested_news57', 'w')
for x in b:
    f.write(x+" : "+str(b[x])+"\n")
f.close()

b1 = datetime.datetime.now()
print(b1 - a1)

master = Tk()
Label(master, text="වචනය").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)
# Button(master, text='Clear', command=e1.delete(0, "end")).grid(row=3, column=2, sticky=W, pady=4)

mainloop()
