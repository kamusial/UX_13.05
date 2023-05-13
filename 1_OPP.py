class Auto:
    def __init__(self, barwa, info_o_kondycji, rok_produkcji):
        self._kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_o_kondycji
        self.__spalanie_na_100 = 14
        self.__tryb_ekonomiczny = False
        self.wiek = 2023 - rok_produkcji
        self.przebieg = 0

    def aktualizacja_przebiegu(self, przebieg):
        if przebieg > 0:
            self.przebieg += przebieg
        else:
            print('zła wartosc')

    def admin_aktualizacja_przebiegu(self, przebieg1, przebieg2):
        if przebieg1 == przebieg2:
            self.przebieg += przebieg1
            print('zmieniles przebieg o ',przebieg1)
            if przebieg1 < 0:
                print('Wysylam maila do prezesa')

    def wlacz_eco(self):
        self.__spalanie_na_100 = 8
        self.__tryb_ekonomiczny = True

    def wylacz_eco(self):
        self.__spalanie_na_100 = 14
        self.__tryb_ekonomiczny = False

    def wyswietl_tryb(self):
        if self.__spalanie_na_100 > 10:
            print('spalanie jest nieco wyzsze')
        else:
            print('spalanie wynosi TYLKO ',self.__spalanie_na_100)

moje_auto = Auto('czerwony', 3, 1965)
# print(moje_auto.__kondycja)
# moje_auto.__kondycja += 1
# print(moje_auto.__kondycja)

moje_auto.wlacz_eco()
moje_auto.wyswietl_tryb()
moje_auto.aktualizacja_przebiegu(20)
print(moje_auto.przebieg)
moje_auto.aktualizacja_przebiegu(-50)
print(moje_auto.przebieg)


