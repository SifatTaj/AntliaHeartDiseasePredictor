import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

Window.clearcolor = (.3, .3, .3, 1)
Window.set_title('Antlia Heart Disease Predictor')


class MyLayout(Widget):
    name = ObjectProperty(None)
    age = ObjectProperty(None)
    sex = ObjectProperty(None)
    cp1 = ObjectProperty(None)
    cp2 = ObjectProperty(None)
    bp = ObjectProperty(None)
    chol = ObjectProperty(None)
    fbs = ObjectProperty(None)
    restecg = ObjectProperty(None)
    thalach = ObjectProperty(None)
    exang = ObjectProperty(None)
    oldpeak = ObjectProperty(None)
    slope = ObjectProperty(None)
    ca = ObjectProperty(None)
    thal = ObjectProperty(None)

    def on_pressed(self):
        print(self.sex.state)


class MyApp(App):
    def build(self):
        self.title = "Antlia Heart Disease Predictor"
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
