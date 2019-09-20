import hashlib


def hashing_tagged_copus():  # hash tagging function for all the unique words in the tagged corpus
    filepath = "cleaned_spell_corrected_corpus.txt"
    a = {}
    with open(filepath) as fp:
        for line in fp:
            x = line.strip().split(' ')  # Get all the unique words in the corpus with their frequencies
            for i in x:
                if i not in a:
                    a[i] = 0
                else:
                    a[i] += 1
    hashed_dic = {}

    for i in a:
        encoded_word = i.encode('utf-8')
        hash_object = hashlib.sha512(encoded_word)  # hash each word in the dictionary
        hex_dig = hash_object.hexdigest()
        if type(a[i]) is int:
            hashed_dic[hex_dig] = a[i]
        else:
            hashed_dic[hex_dig] = 0

    sorted_hashed_dic1 = sorted(hashed_dic.items(), key=lambda kv: kv[1])
    sorted_hashed_dic = sorted_hashed_dic1[::-1]

    return sorted_hashed_dic


b = hashing_tagged_copus()
print(len(b))
f = open('hashed_dic2', 'w')
for x in b:
    f.write(x[0]+" "+str(x[1])+"\n")
f.close()