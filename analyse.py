import hashlib

from pyfasttext import FastText

from itertools import permutations


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


def hashing_tagged_copus():
    filepath = "hashed_dic"
    a = {}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')
            a[x[0]] = int(x[1])
    return a


def get_hash(word):
    encoded_word = word.encode('utf-8')
    hash_object = hashlib.sha512(encoded_word)
    hex_dig = hash_object.hexdigest()
    return hex_dig


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


def nana_lala(word):  # function which generates permutations of a given word
    # Get all permutations of length 2
    # and length 2
    all = ['න', 'ණ', 'ල', 'ළ', 'ශ', 'ෂ', 'ත', 'ථ', 'බ', 'භ', 'ද', 'ධ', 'ග', 'ඳු', 'දු', 'ු', 'ූ', 'ට', 'ඨ', 'ච', 'ඡ',
           'ජ']
    # simple = ['න', 'ල', 'ශ', 'ත', 'බ', 'ද']
    # capital = ['ණ', 'ළ', 'ෂ', 'ථ', 'භ', 'ධ']
    # indices = []
    # word_lst = []
    permutated_words = [word]
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
            Dhaword = False
            if word_lst[i[j]] == 'න':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ණ'

            if word_lst[i[j]] == 'ණ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'න'

            if word_lst[i[j]] == 'ල':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ළ'

            if word_lst[i[j]] == 'ළ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ල'

            if word_lst[i[j]] == 'ශ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ෂ'

            if word_lst[i[j]] == 'ෂ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ශ'

            if word_lst[i[j]] == 'ත':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ථ'

            if word_lst[i[j]] == 'ථ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ත'

            if word_lst[i[j]] == 'බ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'භ'

            if word_lst[i[j]] == 'භ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'බ'

            if word_lst[i[j]] == 'ද':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ධ'
                per_word2[i[j]] = 'ඳ'
                Dhaword = True
            if word_lst[i[j]] == 'ධ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ද'

            if word_lst[i[j]] == 'ග':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඟ'

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

            if word_lst[i[j]] == 'ූ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ු'

            if word_lst[i[j]] == 'ට':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඨ'

            if word_lst[i[j]] == 'ඨ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ට'

            if word_lst[i[j]] == 'ඡ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ච'
                per_word2[i[j]] = 'ජ'
                Dhaword = True
            if word_lst[i[j]] == 'ච':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'

            if word_lst[i[j]] == 'ජ':
                if j <= 0:
                    per_word = word_lst.copy()
                    per_word2 = word_lst.copy()
                per_word[i[j]] = 'ඡ'

        concat = ''
        for k in per_word:
            concat += k
        if Dhaword:
            concat2 = ''
            for k in per_word2:
                concat2 += k

            hash_dig = get_hash(concat2)
            if hash_dig in hashed_dic:
                permutated_words.append(concat2)
        hash_dig = get_hash(concat)
        if hash_dig in hashed_dic:
            permutated_words.append(concat)
    return permutated_words


def is_papili_missing_word(word1, word2):
    array = []
    for i in word2:
        array.append(i)
    for i in word1:
        if i in array:
            array.remove(i)

    if len(array) > 0:
        if array[0] == 'ු' or array[0] == 'ූ' or array[0] == '්' or array[0] == 'ා' or array[0] == 'ි' or array[
            0] == 'ී' or array[0] == 'ෑ' or array[0] == 'ැ':
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


filepath2 = "extracted_corrected_official"
extracted_corrected = []
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_corrected.append(x[0])

filepath2 = "extracted_corrected_news"
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_corrected.append(x[0])

filepath2 = "extracted_corrected_nimasha"
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_corrected.append(x[0])

filepath2 = "extracted_misspelled_official"
extracted_misspelled = []
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_misspelled.append(x[0])

filepath2 = "extracted_misspelled_news"
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_misspelled.append(x[0])

filepath2 = "extracted_misspelled_nimasha"
with open(filepath2) as fp:
    for line in fp:
        x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
        extracted_misspelled.append(x[0])

min_edit = []
min1_count = 0
min2_count = 0
min3_count = 0
min_other_count = 0
min2_frequency = {}
hashed_dic = hashing_tagged_copus()
# model = FastText('sinhala_all2.bin')
# words = model.nearest_neighbors('ප්‍රමාණය', k=2000)
# print(words)
nana_lala_errors = 0
ispili_missing_errors = 0
joiner_missing_word = 0
insetion = 0
insetion_dic = {}
deletiion = 0
deletiion_dic = {}
substitute = 0
substitute_dic ={}
if is_papili_missing_word('අනතුරැව', 'අනතුරුව'):
    ispili_missing_errors += 0
fastztext_top = {}
ispipiWords =[]
ipsli_missing_dic = {}
is_papili_missing_word('විෂය', 'විය')
for i in range(len(extracted_corrected)):
    # words = model.nearest_neighbors(extracted_misspelled[i], k=2000)
    # fastztext_top[words[0][0]] = words[0][1]
    min_edit_distance = levenshtein(extracted_misspelled[i], extracted_corrected[i])
    if min_edit_distance == 2:
        min1_count += 1
    elif min_edit_distance == 1:
        min2_count += 1
        if len(extracted_misspelled[i]) == len(extracted_corrected[i]):
            substitute += 1
            substitute_dic[extracted_corrected[i]] = extracted_misspelled[i]
        if len(extracted_misspelled[i]) > len(extracted_corrected[i]):
            deletiion += 1
            deletiion_dic[extracted_corrected[i]] = extracted_misspelled[i]
        if len(extracted_misspelled[i]) < len(extracted_corrected[i]):
            insetion += 1
            insetion_dic[extracted_corrected[i]] = extracted_misspelled[i]
        # if get_hash(extracted_corrected[i]) in hashed_dic:
        #     min2_frequency[extracted_corrected[i]] = hashed_dic[get_hash(extracted_corrected[i])]
        #     words = model.nearest_neighbors(extracted_misspelled[i], k=2000)
        # arr =[]
        # for j in words:
        #     min_edit_distance = levenshtein(j[0], extracted_corrected[i])
        #     if min_edit_distance <= 2:
        #         arr.append(j)
        # print(arr[0])
        # fastztext_top[arr[0][0]] = arr[0][1]

    elif min_edit_distance == 3:
        min3_count += 1
    else:
        min_other_count += 1


    min_edit.append(min_edit_distance)
    if extracted_corrected[i] in nana_lala(extracted_misspelled[i]):
        nana_lala_errors += 1
    if is_papili_missing_word(extracted_misspelled[i], extracted_corrected[i]) and levenshtein(extracted_misspelled[i], extracted_corrected[i])<=1:
        ispili_missing_errors += 1
    if is_papili_missing_word(extracted_misspelled[i], extracted_corrected[i]) and not levenshtein(extracted_misspelled[i], extracted_corrected[i])<=1:
        ipsli_missing_dic[extracted_corrected[i]] = extracted_misspelled[i]
        is_papili_missing_word(extracted_misspelled[i], extracted_corrected[i])
        ispipiWords.append(extracted_corrected[i])
    if is_joiner_missing_word(extracted_misspelled[i], extracted_corrected[i]):
        joiner_missing_word += 1
print(len(extracted_misspelled), len(extracted_corrected))
print(min1_count)
print(insetion)
# print(insetion_dic)
print(deletiion)
# print(deletiion_dic)
print(substitute)
# print(substitute_dic)
print(min2_count)
print(min3_count)
print(min_other_count)
# print(min2_frequency)
# print(min_edit)
print(nana_lala_errors)
print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
print(ispili_missing_errors)
# print(ipsli_missing_dic)
print(joiner_missing_word)
# f = open('Analyse', 'w')
# for x in fastztext_top:
#     f.write(str(fastztext_top[x])+"\n")
# f.close()
word1 = 'ප්\u200dරමාණය'
word2 = 'ප්රමාණය'  # wrong
word3 = 'ප්‍රමාණය'
if is_joiner_missing_word(word2, word1):
    print('KKKKKKKKKKKKKKKKKKKKKKKKKKKK')
if word1 == word2:
    print("GGGGGGGGGGGGGGGGGGGGGG")
if word1 == word3:
    print("DDDDDDDDDDDDDDDDDDDDDDDDD")
