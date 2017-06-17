#!/usr/bin/env python
# _*_ coding: UTF-8 _*_




#Python 3

import re


fp = open("sample.txt","r")
article = fp.read()
new_article = re.sub("[^a-zA-Z\s]","",article)

words = new_article.split()

words_count = {}

for word in words:
    if word.upper() in words_count:
        words_count[word.upper()] = words_count[word.upper()] + 1
    else:
        words_count[word.upper()] = 1

key_list = list(words_count.keys())
key_list.sort()

for key in key_list:
    if words_count[key] > 1:
        print("{}:{}".format(key,words_count[key]))

