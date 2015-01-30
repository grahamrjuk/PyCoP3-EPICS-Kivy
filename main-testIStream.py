import kivy
kivy.require('1.8.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label

from kivy.clock import Clock
from imageStreamer.image_streamer import ImageStream

class KivyEpicsApp(App):

    def build(self):
        is_widget = ImageStream()
        is_widget.set_ca_name('PICTURE')
        Clock.schedule_interval(is_widget.update, 1.0 / 60.0)
        Clock.schedule_interval(is_widget.set_new_data, 1.0/4.0)
        return is_widget


if __name__ == '__main__':
    KivyEpicsApp().run()
