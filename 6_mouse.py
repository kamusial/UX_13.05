import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty()
    def on_touch_down(self, touch):
        self.btn.opacity = 0.5
        print('Mouse down ',touch)
    def on_touch_move(self, touch):
        print('mouse move ',touch)
    def on_touch_up(self, touch):
        print('mouse up ',touch)
        self.btn.opacity = 1


class My6App(App):
    def build(self):
        return Touch()

if __name__ == "__main__":
    My6App().run()