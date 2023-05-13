import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Imie: "))
        self.imie = TextInput(multiline=False)
        self.inside.add_widget(self.imie)

        self.inside.add_widget(Label(text="Nazwisko: "))
        self.nazwisko = TextInput(multiline=False)
        self.inside.add_widget(self.nazwisko)

        self.inside.add_widget(Label(text="rok_urodzenia: "))
        self.rok_urodzenia = TextInput(multiline=False)
        self.inside.add_widget(self.rok_urodzenia)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_size=42)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        print('wcisniety')
        imie = self.imie.text
        nazwisko = self.nazwisko.text
        rok_urodz = self.rok_urodzenia.text
        print(f'Imię: {imie}, nazwisko: {nazwisko}\nrok urodzenia: {rok_urodz}')

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()