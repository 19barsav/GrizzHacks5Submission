# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 02:31:07 2020

@author: savan
"""

import string
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords


def analyze(text):
        
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    print("uhm ", text)
    token_words = wt(text,'english')
    complete_words = ''' '''
    for word in token_words:
        if word not in stopwords.words('english'):
            complete_words += ' ' + word
   
                
    s_count = sexual_count(complete_words)
    p_count = physical_count(complete_words)
    ss_count = slurs_count(complete_words)
        
    if (s_count == 0) and (p_count == 0) and (ss_count == 0):
        return "Good news! Content warning are not applicable to this literature!"
    else:
        output = """   """
        s = "There are " + str(s_count) + " instances of sexually violent word(s).\n"
        p = "There are " + str(p_count) + " instances of physically violent word(s).\n"
        ss = "There are " + str(ss_count) + " instances of slur(s)."
        output = s + p + ss 
        return output
                
                
def sexual_count(complete_text):
    
    
    print(complete_text)
    emotion_list = []
    with open('sexual.txt', 'r', encoding='utf-8') as file:
        for line in file:
            emotion = line.strip()
            n = complete_text.count(emotion)
            emotion_list.append([emotion, n])
    total = 0
    for i in emotion_list:
        print (i[0])
        print (int(i[1]))
        total += int(i[1])
    
    return total
        
def physical_count(complete_text):
    print(complete_text)
    emotion_list = []
    with open('physical.txt', 'r', encoding='utf-8') as file:
        for line in file:
            emotion = line.strip()
            n = complete_text.count(emotion)
            emotion_list.append([emotion, n])
    total = 0
    for i in emotion_list:
        print (i[0])
        print (int(i[1]))
        total += int(i[1])
    
    return total
        
        
def slurs_count(complete_text):
    print(complete_text)
    emotion_list = []
    with open('slurs.txt', 'r', encoding='utf-8') as file:
        for line in file:
            emotion = line.strip()
            n = complete_text.count(emotion)
            emotion_list.append([emotion, n])
    total = 0
    for i in emotion_list:
        print (i[0])
        print (int(i[1]))
        total += int(i[1])
    
    return total
        