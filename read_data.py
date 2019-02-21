import os
import json
import nltk
from collections import Counter, defaultdict
from string import punctuation
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import unicodedata

DATA = "./data"
POSTS_DATA ="./data/posts"
MESSAGES_DATA ="./data/messages"
COMMENTS_DATA ="./data/comments"

def read_message(data_path):
    # tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    texts = []  # list of text samples
    doc = []
    words_train = 0
    stemmer = SnowballStemmer("english")
    for name in sorted(os.listdir(data_path)):
        path = os.path.join(data_path, name)

        if os.path.isdir(path):
            for fname in sorted(os.listdir(path)):
                fpath = os.path.join(path, fname)
                data = read_file(fpath)
        else:
            data = read_file(path)

        # for item in data["comments"]:
        #     print(item["data"][0]["comment"]["comment"])
        #     tmp = unicodedata.normalize('NFKD', item["data"][0]["comment"]["comment"]).encode('ascii','ignore')
        #     print(tmp)
        return
        # print(data[0])
                # print(t)
                # text = bs.BeautifulSoup(t, 'xml')
                # data = text.TEXT.string
                # tmp = unicodedata.normalize('NFKD', data).encode('ascii','ignore')
                # # print(tmp)
                # sents = sent_tokenize(tmp.decode("ascii"))
                # for sent in sents:
                #     if sent.strip():                        
                        
                        # words_arrays = re.findall(r"[\w']+|[.,!?;\/+]", sent.strip().lower())

                        # #remove date in sentence
                        # sentence = [word for word in words_arrays \
                        # if not re.search(r'[0-9]{1,4}[\/,:,-][0-9]{1,3}([\/,:,-][0-9]{2,4})?([\/,:,-][0-9]{2,4})?', word)]

                        # sentence = [word for word in sentence if not re.search(r'\'s', word)]

                        # #remove specials symbols
                        # sentence = [c for c in sentence if c not in \
                        # ('!','.',':', '-', '+', '_', '(', ')', '*', '&', '#', ';', '?', '>', '<', '%', \
                        #     '{', '}', '=', ',', ']', '[', '`', '\'')]

                        # #remove // in text
                        # sentence = [c for c in sentence if not re.search(r'^/[/]?', c)]

                        # #remove ________ in text
                        # sentence = [c for c in sentence if not re.search(r'_+', c)]

                        # #split string 123tert to 123 tert
                        # sentence = [c for word in sentence for c in re.split(r'([0-9]*)([a-zA-Z\'0-9]+)', word) \
                        # if c]
                        # #remove measure weight/digits in sentence
                        # sentence = [word for word in sentence if not re.search(r'^\d+\.*\s?\d*\s?[mg]*$', word)]
                        # sentence = [c for c in sentence if not re.search(r'^mg', c)]
                        

                        # sentence = [c for c in sentence if not re.search(r'``|\'\'', c)]

                        # #remove stopwords in sentence
                        # # process_words = [word for word in sentence if word not in stopwords.words('english')]

                        # #stemming words in sentences
                        # # process_words = [stemmer.stem(t) for t in process_words]

                        # #tokenizer sentence
                        # words_train += len(sentence)
                        # texts.append(sentence)
    # return texts, words_train


def read_file(file_path):
    with open(file_path, encoding='raw_unicode_escape') as data_file:
        data = json.loads(data_file.read().encode('raw_unicode_escape').decode())
        for item in data["comments"]:
            print(item["data"][0]["comment"]["comment"])
            tmp = unicodedata.normalize('NFKD', item["data"][0]["comment"]["comment"]).encode('ascii','ignore')
            print(tmp)
    return data

# print(chr('\u2020'))
read_message(COMMENTS_DATA)