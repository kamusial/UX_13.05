100 osób, każdy człowkiek ma imie, nazwisko, mail, wiek, wypłata
20 aut, każde, rejestracja, przebieg, kolor

pracownik1_imie = 'Adam'
pracownik2_imie = 'Andrzej'
pracownik2_nazwisko = 'Nowak'

LISTY:
pracownik1 = ['Adam', 'kowalski', '', 36, 4657.23]

pracownik[3][3]
auta[3][2]

def nadaj_mail(index_pracownika):
    pracownik[index_pracownika][2] = index_pracownika[0]+'.'+index_pracownika[2]+'@firma.com'

def dodaj_przebieg(index_auta, przebieg):
    auta[index_auta][1] += przebieg

pracownik[5][3] = 'mama'



