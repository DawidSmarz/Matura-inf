with open("zadanie_63/ciagi.txt", "r") as plik:
    dane = [int(x) for x in plik]

for liczba in dane:
    x = str(liczba)
    dlugosc_ciagu = len(x)

    czy_podzielna = dlugosc_ciagu % 2
    if czy_podzielna == 0:
        polowa_dlugosci_ciagu = dlugosc_ciagu // 2

        lewa = x[:polowa_dlugosci_ciagu]
        prawa = x[polowa_dlugosci_ciagu:]

        if lewa == prawa:
            print(x)
