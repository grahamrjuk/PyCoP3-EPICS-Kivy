import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label


class KivyEpicsApp(App):

    def build(self):
        return Label(text='Hello Epics from Kivy')


if __name__ == '__main__':
    KivyEpicsApp().run()
