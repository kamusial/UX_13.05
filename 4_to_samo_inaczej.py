import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGrid(Widget):
    imie = ObjectProperty()
    nazw = ObjectProperty()
    rok = ObjectProperty()

    def btn(self):
        print(f'{self.imie.text}, {self.nazw.text}')
        self.imie.text = ''
        self.nazw.text = ''
        self.rok.text = ''

class My4App(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    My4App().run()