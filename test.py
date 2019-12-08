import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

Window.clearcolor = (.3, .3, .3, 1)


# class FloatLayout(Widget):
#     name = ObjectProperty(None)
#
#     def on_pressed(self):
#         print(self.name.text)


class MyApp(App):
    def build(self):
        return FloatLayout()


if __name__ == "__main__":
    MyApp().run()
