# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:30:39 2020

@author: savan

import nltk
nltk.download()
"""

import os
import urllib.request as ur
import urllib.parse as up
import re
import string
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords
from collections import Counter

os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')


def start():
    url_words = "https://en.wikipedia.org/wiki/Feminism"
    try:
        text = pull_data(url_words)
    except:
        text = url_words
    output_text = analyze(text)
    print(output_text)
    
    
    
def pull_data(url):
    
    url = url
    values = {'s':'basics',
          'submit':'search'}  
    data = up.urlencode(values)
    data = data.encode('utf-8')  
    req = ur.Request(url, data)
    resp = ur.urlopen(req)
    respData = resp.read()
    paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
    text = ''' '''
    for eachP in paragraphs:
        text = text + ' ' + eachP
    return text

def analyze(text):
    
    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))
    print(text)
    token_words = wt(text,'english')
    print(token_words)
    complete_text = []
    for word in token_words:
        if word not in stopwords.words('english'):
            complete_text.append(word)
            
    s_count = sexual_count(complete_text)
    p_count = physical_count(complete_text)
    slurs_count = slurs_count(complete_text)
    
    if (s_count == 0) and (p_count == 0) and (slurs_count == 0):
        return "Good news! Content warning are not aplicable to this literature!"
    else:
        output = """   """
        s = "There are " + s_count + " instances of sexually violent words."
        p = "There are " + p_count + " instances of physically violent words."
        ss = "There are " + slurs_count + " instances of physically violent words."
        output = s + p + ss
        return output
            
            
def sexual_count(complete_text):
    emotion_list = []
    with open('sexual.txt', 'r') as file:
        for line in file:
            emotion = line.strip()
            if emotion in complete_text:
                emotion_list.append(emotion)
    print(emotion_list)
    w = Counter(emotion_list)
    print(w)
    return w
    
def physical_count(complete_text):
    emotion_list = []
    with open('physical.txt', 'r') as file:
        for line in file:
            emotion = line.strip()
            if emotion in complete_text:
                emotion_list.append(emotion)
    print(emotion_list)
    w = Counter(emotion_list)
    print(w)
    return w
    
def slurs_count(complete_text):
    emotion_list = []
    with open('slurs.txt', 'r') as file:
        for line in file:
            emotion = line.strip()
            if emotion in complete_text:
                emotion_list.append(emotion)
    print(emotion_list)
    w = Counter(emotion_list)
    print(w)
    return w
    

    
    
    
    

def main():
    start()
    
    
        
if __name__ == "__main__":
    main()
 