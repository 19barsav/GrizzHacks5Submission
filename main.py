import webbrowser
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog

import os
import urllib.request as ur
import urllib.parse as up
import re
from helper import analyze
from google.cloud import vision
from google.cloud.vision import types
from kivy.uix.popup import Popup
from kivy.config import Config 
Config.set('graphics', 'resizable', True)

os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

ContentDepoBar = '''
MDTextField:
    hint_text: "Enter URL, Image URL or Article Transcription"
    pos_hint: {'center_x':0.5, 'center_y':0.5}
    size_hint_x: 0.7
    size_hunt_y: 0.5
    width: 300
    height: 2
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
          
      
        screen.add_widget(self.ContentDepository)
        screen.add_widget(submitButton)
        screen.add_widget(submitButton2)
            #The "on_release" detail here is where the user is submitting their URL. accessing that information
            #happens below in the display_cw function. 
     
        close_openingMessage = MDFlatButton(text='Close', on_release=self.close_opening)
        about_button = MDFlatButton(text='About', on_release=self.open_about)
        resources_button = MDFlatButton(text='Resources', on_release=self.open_resources)
        self.openingMessage = MDDialog(text='Content Warning is an application designed to protect readers and researchers from triggering or volatile content. Submit a website URL, text snippet, or image URL of a document/handwriting and the program will inform you of any necessary content warnings - without exposing the details.',\
                    size_hint=(0.7,1), pos_hint={'center_x':0.5, 'center_y':0.75}, buttons=[resources_button, about_button, close_openingMessage])
        
        
       
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
        
    def close_dialog2(self, obj):
        self.about_message.dismiss()
    def close_resources(self, obj):
        self.resources_message.dismiss()
    def open_about(self, obj):
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog2)
        output_text ='We are a team of three social justice minded developers, who are using our ' + \
                                      ' Grizzhacks 5 project as a way to make the internet a safer and less surprising place. As a team, ' + \
                                      ' we strongly believe in blending computer science with the social sciences to create more mindful ' + \
                                      ' and socially-aware programs. Content Warning was born out of wanting to make researchers and ' + \
                                      ' everyday users aware of the potentially harmful topics or phrases in assigned readings, researched ' + \
                                      ' articles, or in any other type of text. '
        self.about_message = MDDialog(text= output_text \
                            , size_hint=(0.7,1), buttons=[close_button])
        self.about_message.open()
    def open_resources(self, obj):
        output_text = 'If you would like to know more about content warnings and why they matter, click the \"Information on Content Warnings\" button.\n\n' + \
                        'If you need access to mental health services, click the \"Mental Health Resources\" button.'
        
        close_button = MDFlatButton(text='Close', on_release=self.close_resources)
        suicide_button = MDFlatButton(text='Information on Content Warnings', on_press=self.mentalhealth_help_web)
        matter_button = MDFlatButton(text='Mental Health Resources', on_press=self.matter)
        self.resources_message = MDDialog(text=output_text\
                            , size_hint=(0.7,1), buttons=[matter_button, suicide_button, close_button])
        self.resources_message.open()
    def mentalhealth_help_web(self, obj):
        webbrowser.open("https://www.cdc.gov/mentalhealth/tools-resources/index.htm")
    def matter(self, obj):
        webbrowser.open("https://sites.lsa.umich.edu/inclusive-teaching/inclusive-classrooms/an-introduction-to-content-warnings-and-trigger-warnings/")
        
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
    
    def image_data(self, url):
        image_uri = url

        client = vision.ImageAnnotatorClient()
        image = vision.types.Image()
        image.source.image_uri = image_uri

        response = client.document_text_detection(image=image)
        text = ''' '''
        for texts in response.text_annotations:
            text = text + ' ' + texts.description.lower()
        return text
    

    
ContentWarning().run()
