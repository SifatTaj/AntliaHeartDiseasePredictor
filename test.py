import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.lang import Builder

from core import model
from core.d_tree import dtc
from core.knn import knn
from core.logistic_regression import lr
from core.naive_bayes import nb
from core.random_forest import rf
from core.svm import svm

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
    result = ObjectProperty(None)

    def on_pressed(self):

        patient = ""

        patient = patient + self.age.text + ","
        patient = patient + ("1" if self.sex.state == "down" else "0") + ","

        if self.cp1.state == "down":
            patient = patient + "3" + ","

        elif self.cp2.state == "down":
            patient = patient + "2" + ","

        else:
            patient = patient + "1" + ","

        patient = patient + self.bp.text + ","
        patient = patient + self.chol.text + ","
        patient = patient + ("1" if int(self.fbs.text) > 120 else "0") + ","

        if self.restecg.text == "normal":
            patient = patient + "0" + ","

        elif self.restecg.text == "ST-T":
            patient = patient + "1" + ","

        else:
            patient = patient + "2" + ","

        patient = patient + self.thalach.text + ","
        patient = patient + ("1" if self.exang.state == "down" else "0") + ","
        patient = patient + self.oldpeak.text + ","

        if self.slope.text == "unsloping":
            patient = patient + "1" + ","

        elif self.slope.text == "flat":
            patient = patient + "2" + ","

        else:
            patient = patient + "3" + ","

        patient = patient + self.ca.text + ","

        if self.thal.text == "normal":
            patient = patient + "1" + ","

        elif self.thal.text == "fixed":
            patient = patient + "2" + ","

        else:
            patient = patient + "3" + ",0"

        print(patient)

        file = open("heart.csv", "a")
        file.write(patient)

        test_knn = knn.predict(model.x_test.T)
        test_dtree = dtc.predict(model.x_test.T)
        test_lr = lr.predict(model.x_test.T)
        test_nb = nb.predict(model.x_test.T)
        test_rf = rf.predict(model.x_test.T)
        test_svm = svm.predict(model.x_test.T)

        # wavg = test_knn * 88.52 + test_svm * 86.89 + test_nb * 86.89 + test_dtree * 80.33 + test_rf * 88.52 + test_lr * 86
        wavg = test_knn + test_svm + test_nb + test_dtree + test_rf + test_lr
        pred = wavg / 6

        if pred[0] > .5:
            self.result.text = "Result: Yes"
        else:
            self.result.text = "Result: No"



class MyApp(App):
    def build(self):
        self.title = "Antlia Heart Disease Predictor"
        return MyLayout()


if __name__ == "__main__":
    MyApp().run()
