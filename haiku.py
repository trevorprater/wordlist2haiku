import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import random
try:
    import ujson as json
except:
    import json

syl_d = json.loads(open('syl_cnt.json').read())
words = []


def construct_line(n_syllables):
    syl_cnt = 0
    haiku_line = []
    while syl_cnt != n_syllables:
        rand_k = random.choice(words)  #syl_d.keys())
        if syl_d[rand_k] + syl_cnt <= n_syllables:
            haiku_line.append(rand_k)
            syl_cnt += syl_d[rand_k]
        if syl_cnt == n_syllables:
            return " ".join(haiku_line).lower()


if __name__ == '__main__':
    words = [w.strip() for w in sys.stdin]

    for i in range(100):
        """
        Generate n haikus
        """
        print construct_line(5)
        print construct_line(7)
        print construct_line(5)
        print '*' * 80
