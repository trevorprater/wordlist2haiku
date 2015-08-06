import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import string
import curses
from curses.ascii import isdigit
from pprint import pprint
try:
    import ujson as json
except:
    import json

import nltk
from nltk.corpus import cmudict

d = cmudict.dict()


def n_syl(word):
    """
    Returns the number of syllables in a word.
    """
    return len([c for c in word if c in [u'\u2022', ' ', '-']]) + 1


def clean_word(word):
    d = {u'\u2022': '', ' ': ''}  #, '-': ''}
    return reduce(lambda x, y: x.replace(y, d[y]), d, word)


if __name__ == '__main__':
    # Read in a dictionary and count the syllables in each word.
    syllables = [unicode(s.strip()) for s in open('syllables.txt').readlines()]
    syl_cnt_d = {clean_word(s): n_syl(s) for s in syllables}
    res_dict = {}

    for ctr, line in enumerate(sys.stdin):
        if ctr > 1:
            word = "".join([c for c in unicode(line.strip())
                            if c not in string.punctuation or c == '-'])
            if syl_cnt_d.get(word, None):
                res_dict[word] = syl_cnt_d[word]

    with open('syl_cnt.json', 'r+') as f:
        f.write(json.dumps(syl_cnt_d))

    for word in res_dict.keys():
        print word
