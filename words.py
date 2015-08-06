"""
Takes a corpus of text located in 'words.txt' and returns a sorted dict of the most commonly occurring words. { word: num_occurrences }
"""

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import string

from nltk.corpus import stopwords

stop_words = stopwords.words("english")
dupe_d = {}

if __name__ == '__main__':
    with open('words.txt') as f:
        for w in [w.replace('\n', '').strip() for w in f.readlines()]:
            try:
                dupe_d[w] += 1
            except:
                dupe_d[w] = 1

        print 'word, count'
        print '*' * len('word, count')

        for w in sorted(dupe_d, key=dupe_d.get, reverse=True):
            if w not in stop_words:
                print "".join([c for c in w
                               if c not in string.punctuation or c == '-'])
