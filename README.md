# wordlist2haiku

This code will accept a list of words and generate n haikus from it. It contains a JSON file that maps every word in the English language to the number of vowels contained within a given word.

I modeled this incredibly brief project with a decoupled, UNIX-like approach in mind. Mostly inspired by this [blogpost](http://www.confluent.io/blog/apache-kafka-samza-and-the-unix-philosophy-of-distributed-data) that praises the benefits of such a system. 

P.S., Writing the documentation took longer than writing the code.

## usage
`python words.py | python syl_cnt.py | python haiku.py`


## notes
This repo offers three useful auxillary-features that an aspiring Pythonista may not be aware of:
* A strategy for accumulating the number of duplicates contained within an iterable:
```
with open('words.txt') as f:
        for w in [w.replace('\n', '').strip() for w in f.readlines()]:
            try:
                dupe_d[w] += 1
                print 'Duplicate detected: {}'.format(dupe_d[w])
            except:
                dupe_d[w] = 1
```
* A concise means of replacing a set of unique characters contained within a string:
```
def clean_word(word):
    2b_replaced = {u'\u2022': '', ' ': '', '-': ''}
    return reduce(lambda x, y: x.replace(y, 2b_replaced[y]), 2b_replaced, word)
```
* A snippet that ranks a dictionary by its values and filters any elements that fail to meet an arbitrary constraint:
```
 for w in sorted(dupe_dict, key=dupe_dict.get, reverse=True):
            if word not in stop_words:
                print "".join([char for char in word
                               if char not in string.punctuation or char == '-'])
  ```


## examples
*****************************************************
file breakfast feedback

state how long ai one rest

current culture mind
*****************************************************
vibration data

text home blue battery turn

physical file want
*****************************************************
time visual tool

humanity one tool come

travel feedback put
*****************************************************
class media free

public know great true via

rest ideally
*****************************************************
science safety place

designed analysis see

new well different
*****************************************************
experiential

access battery red come

ways another learn
*****************************************************
building city sense

error really test blue

iteration rest
*****************************************************
character show screen

individual city

scene aspect also
*****************************************************
time infrastructure

turn error planning string plan

public address head
*****************************************************
uncle thinking made

ideally another

exactly system
*****************************************************
