#-*- coding: utf-8 -*- 
#执行语句 type somefile.txt | python stdin.py
import  sys 
text = sys.stdin.read()
word = text.split()
wordcount = len(word)
print wordcount