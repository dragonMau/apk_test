import random

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

kivy.require('1.9.0')

class MyRoot(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def generate_number(self):
        self.random_label.text = str(random.randint(0, 1000))

class Main(App):
    def build(self):
        return MyRoot()


Main().run()
