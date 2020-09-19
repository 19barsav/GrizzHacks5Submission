# -*- coding: utf-8 -*-

import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout

import os
import urllib.request as ur
import urllib.parse as up
import re
import string
from nltk.tokenize import word_tokenize as wt
from nltk.corpus import stopwords
from collections import Counter
from helper import analyze

os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

ContentDepoBar = '''
MDTextField:
    multiline: True
    hint_text: "Enter URL, Image URL or Article Transcription"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: None
    width: 300
'''

class ContentWarning(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A400'
        self.theme_cls.theme_style = 'Dark'
        screen = Screen()
        self.ContentDepository = Builder.load_string(ContentDepoBar)
        submitButton = MDFillRoundFlatButton(text='Submit URL or Paste Test',  pos_hint={'center_x':0.5, 'center_y':0.4}, \
                                             on_release = self.display_cw)  
        submitButton2 = MDFillRoundFlatButton(text='Submit Image URL', pos_hint={'center_x':0.5, 'center_y':0.3}, \
                                             on_release = self.display_cw2) 
            #The "on_release" detail here is where the user is submitting their URL. accessing that information
            #happens below in the display_cw function.
        close_openingMessage = MDFlatButton(text='Close', on_release=self.close_opening)
        self.openingMessage = MDDialog(text='Content Warning is a program designed to protect readers and researchers from triggering or volatile content. Submit a URL, full copy or even a URL of a picture of a body of text, and the program will inform you of any possibly volatile or explicit content.',\
                    size_hint=(0.7,1), pos_hint={'center_x':0.5, 'center_y':0.75}, buttons=[close_openingMessage])
        screen.add_widget(self.ContentDepository)
        screen.add_widget(submitButton)
        screen.add_widget(submitButton2)
            #The "on_release" detail here is where the user is submitting their URL. accessing that information
            #happens below in the display_cw function. 
        self.openingMessage.open()
        
       # scrollTest = ScrollView()
        #scrollTest.add_widget(screen)
        return screen
        
        
    
    def display_cw(self, obj): #import elements from your code to be used in this display message
        contentList = self.ContentDepository.text  #this variable contentList is verbatim the user input
        output_text = self.start(contentList, 1)
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.cwMessage = MDDialog(text=output_text\
                            , size_hint=(0.7,1), buttons=[close_button])
        self.cwMessage.open()
        #The line above establishes a dialog box as whatever Sav wants it to be. text can be equal to however
        #you end up fabricating the Content Warning List. Insert a variable or something of the like.
        
    def display_cw2(self, obj): #import elements from your code to be used in this display message
        contentList = self.ContentDepository.text  #this variable contentList is verbatim the user input
        output_text = self.start(contentList, 2)
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.cwMessage = MDDialog(text=output_text\
                            , size_hint=(0.7,1), buttons=[close_button])
        self.cwMessage.open()
        #The line above establishes a dialog box as whatever Sav wants it to be. text can be equal to however
        #you end up fabricating the Content Warning List. Insert a variable or something of the like.
        
    def close_dialog(self, obj):
        self.cwMessage.dismiss()
        
    def close_opening(self, obj):
        self.openingMessage.dismiss()
    def start(self, contentList, num):
        url_words = contentList
        if num == 1:
            try:
                text = self.pull_data(url_words)
            except:
                text = url_words
        else:
            text = self.image_data(url_words)
        output_text = analyze(text)
        return output_text
      
        
    def pull_data(self, url):
        
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
    
    
    

    
ContentWarning().run()