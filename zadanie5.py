f = open("liczby.txt")
wynik = open("wynik.txt", "w")
#print(f.read())

# for line in f:
#     line = line.strip()
#     print(line)

dane_int = []
dane_str = []
for line in f:
    dane_int.append(int(line))
    dane_str.append(line.strip())
# print(dane_int)
# print(dane_str)

#zadanie 5.1

dane_parzyste = []
for element in dane_int:
    if element % 2 == 0:
        dane_parzyste.append(element)
najwieksza = max(dane_parzyste)
# print(dane_parzyste)
print(najwieksza)
wynik.write("Zadanie 5.1\n")
wynik.write(str(najwieksza) + '\n')

#zadanie 5.2

wynik.write("Zadanie 5.2\n")
for element_p in dane_str:
    if element_p == element_p[ : : -1]:
        wynik.write(element_p + '\n') 
