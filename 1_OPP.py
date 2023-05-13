class Auto:
    def __init__(self, barwa, info_o_kondycji, rok_produkcji):
        self.kolor = barwa
        self.ilosc_paliwa = 10
        self.kondycja = info_o_kondycji
        self.spalanie_na_100 = 14
        self.tryb_ekonomiczny = False
        self.wiek = 2023 - rok_produkcji


