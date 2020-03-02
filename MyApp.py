from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Rectangle, Color
from kivy.properties import NumericProperty


class HomeWindow(Screen):
    rect1 = ObjectProperty(None)
    rect2 = ObjectProperty(None)
    rect3 = ObjectProperty(None)
    rect4 = ObjectProperty(None)
    rect5 = ObjectProperty(None)
    rect6 = ObjectProperty(None)
    rect7 = ObjectProperty(None)
    rect8 = ObjectProperty(None)
    rect9 = ObjectProperty(None)
    rect10 = ObjectProperty(None)
    rect11 = ObjectProperty(None)
    rect12 = ObjectProperty(None)
    rect13 = ObjectProperty(None)
    rect14 = ObjectProperty(None)
    rect15 = ObjectProperty(None)
    rect16 = ObjectProperty(None)
    rect17 = ObjectProperty(None)
    rect18 = ObjectProperty(None)
    rect19 = ObjectProperty(None)
    rect20 = ObjectProperty(None)
    rect21 = ObjectProperty(None)
    rect22 = ObjectProperty(None)
    rect23 = ObjectProperty(None)
    rect24 = ObjectProperty(None)

    rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8, rect9, rect10, rect11,
             rect12, rect13, rect14, rect15, rect16, rect17,
             rect18, rect19, rect20, rect21, rect22, rect23, rect24]
    def displayHistogram(self, numLandfill, numRecycle, numFoodWaste):
        for i in range(numLandfill):
            self.rects[i].background_color = (0, 0.2, 0.8, 1)
        for i in range(numLandfill):
            self.rects[i].background_color = (0, 0.2, 0.8, 1)
        for i in range(numLandfill):
            self.rects[i].background_color = (0, 0.2, 0.8, 1)

class ArchiveWindow(Screen):
    pass

class AddWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass
#loads the kv file

kv = Builder.load_file("my.kv")

class MyMainApp(App, ):
    def build(self):
        return kv

if __name__ == "__main__":
    MyMainApp().run()