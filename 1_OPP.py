class Auto:
    def __init__(self, barwa, info_o_kondycji, rok_produkcji):
        self._kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_o_kondycji
        self.__spalanie_na_100 = 14
        self.__tryb_ekonomiczny = False
        self.wiek = 2023 - rok_produkcji

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



