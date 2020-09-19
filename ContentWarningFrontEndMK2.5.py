# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 20:32:56 2020

@author: VinVigo
"""

import kivymd
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel, MDIcon
# from kivymd.uix.screen import Screen
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.button import MDFillRoundFlatButton, MDFlatButton
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import MDList
# from screen_nav import screens

screens = '''

ScreenManager:
    MenuScreen:
    OperationScreen:

<MenuScreen>:
    name: 'menu'
    MDLabel:
        text: 'Content Warning is a program designed to protect readers and researchers from triggering or volatile content. Submit a URL, full copy or even a URL of a picture of a body of text, and the program will inform you of any possibly volatile or explicit content.'
        pos_hint: {'center_x':0.5, 'center_y':0.75}
        size_hint_x:0.7
        size_hint_y:0.7
    MDFillRoundFlatButton:
        text: 'Go!'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
        on_press: root.manager.current = 'operation'
        
<OperationScreen>:
    name: 'operation'
    MDTextField:
        name: 'ContentDepository'
        hint_text: "Enter URL, Image URL or Article Transcription"
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        size_hint_x:0.7
        width: 300
        multiline: True
    MDFillRoundFlatButton: 
        name: 'button'
        text: 'Process'
        pos_hint: {'center_x':0.5, 'center_y':0.25}
        on_press: self.display_cw()
'''

class MenuScreen(Screen):
    pass

class OperationScreen(Screen):
    pass

screenManage = ScreenManager()

class ContentWarning(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.primary_hue = 'A400'
        self.theme_cls.theme_style = 'Dark'
        #screen = Builder.load_string(screens)
        submitButton = MDFillRoundFlatButton(text='Submit', pos_hint={'center_x':0.5,\
                                                             'center_y': 0.5}, \
                                             on_release = display_cw)
        OperationScreen.add_widget(submitButton)
        screenManage.add_widget(MenuScreen(name='menu'))
        screenManage.add_widget(OperationScreen(name='operation')
        #screen = Screen()
        #self.submitButton = MDFillRoundFlatButton(text='Submit', pos_hint={'center_x':0.5,\
        #                                                     'center_y': 0.5}, \
        #                                     on_release = self.display_cw)
        
       # MenuScreen = Screen()
       # menuLabel = MDLabel(text='Content Warning is a program designed to protect readers and researchers from triggering or volatile content. Submit a URL, full copy or even a URL of a picture of a body of text, and the program will inform you of any possibly volatile or explicit content.',\
       #                    pos_hint={'center_x':0.5, 'center_y':0.75}, size_hint_x=0.7, size_hint_y=0.7)
      #  menuButton = MDFillRoundFlatButton(text='Go!', pos_hint={'center_x':0.5, 'center_y':0.25}, on_press=root.manager.current = 'operation')
       # OperationScreen = Screen()
            
       # sm = ScreenManager()
        
            
        #OperationScreen(name='operation').add_widget(self.submitButton)
        
       
        
        screen=Builder.load_string(screens)
        
          
            #The "on_release" detail here is where the user is submitting their URL. accessing that information
            #happens below in the display_cw function. 
       # screen.add_widget(submitButton)
       # screen.add_widget(self.ContentDepository)
       
        
       return screen
    
    def display_cw(self, obj): #import elements from your code to be used in this display message
        contentList = self.screen.OperationScreen.ContentDepository.text #this variable contentList is verbatim the user input
        close_button = MDFlatButton(text='Close', on_release=self.close_dialog)
        self.cwMessage = MDDialog(text='This message indicates that Sav Hasn\'t yet customized the dialog!'\
                            , size_hint=(0.7,1), buttons=[close_button])
        self.cwMessage.open()
        #The line above establishes a dialog box as whatever Sav wants it to be. text can be equal to however
       #you end up fabricating the Content Warning List. Insert a variable or something of the like.
    def close_dialog(self, obj):
        self.cwMessage.dismiss()
        
    def cw_graph(self, obj):
        self.cwMessage.dismiss()
        
ContentWarning().run()