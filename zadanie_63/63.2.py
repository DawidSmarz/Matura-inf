with open("zadanie_63/ciagi.txt", "r") as plik:
    dane = [int(x) for x in plik]

liczba_ciagow = 0

for liczba in dane:
    ciag = str(liczba)
    if "11" not in ciag:
        liczba_ciagow+=1
        print(liczba_ciagow)
