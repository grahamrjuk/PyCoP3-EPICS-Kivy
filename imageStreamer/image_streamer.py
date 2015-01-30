# Receive data from the PICTURE PV in through the ChannelAccessWrapper

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture

try:
    from channel_access.channel_access_wrapper import ChannelAccessWrapper
except:
    ChannelAccessWrapper = None
    print('No ChannelAccessWrapper')

from random import randint

# create a 64x64 texture, defaults to rgb / ubyte
texture = Texture.create(size=(64, 64))

# create 64x64 rgb tab, and fill with values from 0 to 255
# we'll have a gradient from black to white
size = 64 * 64 * 3
buf = [int(x * 255 / size) for x in range(size)]

# then, convert the array to a ubyte string
buffer = b''.join(map(chr, buf))

# that's all ! you can use it in your graphics now :)
# if self is a widget, you can do this


class ImageStream(Widget):

    def set_ca_name(self, ca_name, test=False):
        self.ca_name = ca_name
        self.ca = None
        if ChannelAccessWrapper:
            self.ca = ChannelAccessWrapper(False)
        self.test = test

    def set_new_data(self, dt=1):
        # then blit the buffer
        buf = [int(x * randint(0,255) / size) for x in range(size)]
        # then, convert the array to a ubyte string
        new_data = b''.join(map(chr, buf))
        if self.ca:
            self.ca.set_pv_value(self.ca_name, new_data)

    def set_texture(self, buf):
        # then blit the buffer
        if buf is not None:
            texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')

    def update(self, dt):
        # doing this for testing - some other part of the app
        # should be putting the data in the Channel
        if self.test:
            self.set_new_data()

        new_data = None
        if self.ca:
            new_data = self.ca.get_pv_value(self.ca_name)

        self.set_texture(new_data)

        with self.canvas:
            Rectangle(texture=texture, pos=self.pos, size=self.size)


class IstreamApp(App):
    def build(self):
        is_widget = ImageStream()
        is_widget.set_ca_name('PICTURE', True)
        Clock.schedule_interval(is_widget.update, 1.0 / 60.0)
        Clock.schedule_interval(is_widget.set_new_data, 1.0 / 4.0)
        return is_widget


if __name__ == '__main__':
    IstreamApp().run()
