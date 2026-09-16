# 🧠 ŚCIĄGA — ALGORYTMY NA MATURĘ Z INFORMATYKI

Ściąga nastawiona na rozpoznawanie algorytmów na kartce i pisanie ich w Pythonie. Nie musisz zapamiętywać wszystkiego słowo w słowo — najważniejsze jest **rozpoznanie schematu**.

---

# 1. Sortowanie bąbelkowe 🫧

## Schemat na kartce

```text
dla j = 1, ..., n-1
    dla i = 1, ..., n-1
        jeżeli A[i] > A[i+1]
            zamień A[i] z A[i+1]
```

## 🔍 Jak rozpoznać?

**Porównuje sąsiednie elementy:**

```text
A[i]  A[i+1]
```

i jeżeli są w złej kolejności → **zamienia je**.

## Python

```python
for j in range(n - 1):
    for i in range(n - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
```

🧠 **HASŁO:** sąsiedzi + zamiana = **BĄBELKOWE**

---

# 2. Sortowanie przez wybieranie 🔎

## Schemat

```text
dla i = 1, ..., n-1
    min = i

    dla j = i+1, ..., n
        jeżeli A[j] < A[min]
            min = j

    zamień A[i] z A[min]
```

## 🔍 Jak rozpoznać?

Algorytm:

**SZUKA MINIMUM → ZAMIENIA JE**

Charakterystyczne:

```text
min = ...
```

## Python

```python
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if A[j] < A[min_index]:
            min_index = j

    A[i], A[min_index] = A[min_index], A[i]
```

🧠 **HASŁO:** szuka minimum → **WYBIERANIE**

---

# 3. Sortowanie przez wstawianie 🃏

Wyobraź sobie układanie kart w ręce.

## Schemat

```text
dla i = 2, ..., n
    x = A[i]
    j = i - 1

    dopóki j >= 1 oraz A[j] > x
        A[j+1] = A[j]
        j = j - 1

    A[j+1] = x
```

## 🔍 Jak rozpoznać?

Charakterystyczne są:

```text
x = A[i]
```

potem:

```text
A[j+1] = A[j]
```

czyli **przesuwanie elementów**, a następnie:

```text
A[j+1] = x
```

## Python

```python
for i in range(1, n):
    x = A[i]
    j = i - 1

    while j >= 0 and A[j] > x:
        A[j + 1] = A[j]
        j -= 1

    A[j + 1] = x
```

🧠 **HASŁO:** bierze element → przesuwa → **WSTAWIA**

---

# 4. Wyszukiwanie liniowe 🔍

Bardzo prosty algorytm.

Chcesz znaleźć np. `7`.

```text
dla i = 1, ..., n
    jeżeli A[i] = 7
        znaleziono
```

## Python

```python
for x in A:
    if x == 7:
        print("Znaleziono")
```

## 🔍 Jak rozpoznać?

Sprawdza elementy **jeden po drugim**:

```text
A[0]
A[1]
A[2]
A[3]
...
```

🧠 **HASŁO:** po kolei → **LINIOWE**

---

# 5. Wyszukiwanie binarne ⚡

Bardzo ważne.

⚠️ **Tablica musi być posortowana.**

Zamiast sprawdzać wszystko po kolei, patrzymy na **środek**.

## Schemat

```text
lewy = 0
prawy = n - 1

dopóki lewy <= prawy
    środek = (lewy + prawy) // 2

    jeżeli A[środek] == szukana
        znaleziono

    jeżeli A[środek] < szukana
        lewy = środek + 1

    w przeciwnym razie
        prawy = środek - 1
```

## 🔍 Jak rozpoznać?

Szukaj:

```text
środek
lewy
prawy
```

i dzielenia zakresu na pół.

🧠 **HASŁO:** środek + połowa → **BINARNE**

---

# 6. NWD — algorytm Euklidesa

**Największy wspólny dzielnik.**

Najważniejszy schemat:

```text
dopóki b ≠ 0
    a, b = b, a mod b
```

## Python

```python
while b != 0:
    a, b = b, a % b

print(a)
```

Przykład:

```text
NWD(48, 18)
```

wynik:

```text
6
```

## 🔍 Jak rozpoznać?

Jeśli widzisz:

```text
a % b
```

i zamianę:

```text
a, b = b, ...
```

→ prawdopodobnie **Euklides**.

🧠 **HASŁO:** `%` + dzielenie z resztą → **NWD**

---

# 7. Liczba pierwsza

Liczba pierwsza ma dokładnie **dwa dzielniki: 1 i samą siebie**.

## Prosty algorytm

```python
def pierwsza(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True
```

## Lepsza wersja

```python
for i in range(2, int(n ** 0.5) + 1):
```

## 🔍 Jak rozpoznać?

Sprawdzanie:

```text
n % i == 0
```

czyli czy liczba dzieli się bez reszty.

🧠 **HASŁO:** `%` → sprawdzanie dzielników.

---

# 8. Rozkład liczby na czynniki pierwsze

Przykład:

```text
60 = 2 × 2 × 3 × 5
```

## Python

```python
n = 60
i = 2

while n > 1:
    if n % i == 0:
        print(i)
        n //= i
    else:
        i += 1
```

## 🔍 Jak rozpoznać?

Algorytm wielokrotnie sprawdza:

```text
n % i == 0
```

a następnie dzieli:

```text
n = n // i
```

🧠 **HASŁO:** dzielimy liczbę aż zostanie `1`.

---

# 9. Silnia

Matematycznie:

```text
n! = 1 × 2 × 3 × ... × n
```

## Python

```python
wynik = 1

for i in range(1, n + 1):
    wynik *= i
```

Np.

```text
5! = 1 × 2 × 3 × 4 × 5 = 120
```

## 🔍 Jak rozpoznać?

Mnożenie kolejnych liczb:

```text
wynik *= i
```

🧠 **HASŁO:** mnożymy od `1` do `n`.

---

# 10. Ciąg Fibonacciego

Ciąg:

```text
0, 1, 1, 2, 3, 5, 8, 13...
```

Każdy element powstaje z dwóch poprzednich.

## Python

```python
a = 0
b = 1

for i in range(n):
    print(a)
    a, b = b, a + b
```

## 🔍 Jak rozpoznać?

Charakterystyczne:

```text
a, b = b, a + b
```

🧠 **HASŁO:** dwa poprzednie → następny.

---

# 11. Rekurencja 🔄

Funkcja **wywołuje samą siebie**.

Przykład silni:

```python
def silnia(n):
    if n == 0:
        return 1

    return n * silnia(n - 1)
```

## 🔍 Jak rozpoznać?

Funkcja w środku ma:

```text
silnia(...)
```

czyli **wywołuje samą siebie**.

Musi mieć również **warunek zakończenia**.

🧠 **HASŁO:** funkcja wywołuje samą siebie.

---

# 12. Sortowanie przez scalanie

## Schemat

```text
podziel tablicę na dwie części

posortuj lewą część
posortuj prawą część

scal obie części
```

## 🔍 Jak rozpoznać?

Szukaj:

```text
scal
merge
lewa część
prawa część
```

oraz często **rekurencji**.

🧠 **HASŁO:** podziel → posortuj → **SCAL**

---

# 13. Quicksort

## Schemat

```text
wybierz pivot

podziel elementy:
    mniejsze → lewa
    większe → prawa

posortuj lewą część
posortuj prawą część
```

## 🔍 Jak rozpoznać?

Najważniejsze słowo:

```text
PIVOT
```

🧠 **HASŁO:** pivot → podział → rekurencja.

---

# 14. Zamiana systemu dziesiętnego na binarny

Bardzo przydatne.

Np. `13`:

```text
13 / 2 → reszta 1
6  / 2 → reszta 0
3  / 2 → reszta 1
1  / 2 → reszta 1
```

Czytamy reszty od dołu:

```text
1101
```

## Python

```python
n = 13

while n > 0:
    print(n % 2)
    n //= 2
```

⚠️ Wypisze reszty od końca, więc trzeba je potem odwrócić.

🧠 **HASŁO:** dzielenie przez `2` + reszty.

---

# 15. Zliczanie elementów

Bardzo częsty schemat.

Pytanie:

> Ile liczb w tablicy jest parzystych?

```text
ile = 0

for x in A:
    if x % 2 == 0:
        ile += 1
```

## 🔍 Jak rozpoznać?

Masz licznik:

```text
ile = 0
```

i później:

```text
ile += 1
```

🧠 **HASŁO:** licznik + warunek.

---

# 🚨 Najważniejsza maturalna mapa

Jeśli dostaniesz algorytm na kartce, szukaj:

```text
A[i] i A[i+1] + zamiana
        ↓
   🫧 BĄBELKOWE
```

```text
min = ... + szukanie najmniejszego
        ↓
   🔎 WYBIERANIE
```

```text
x = A[i] + przesuwanie + wstawienie
        ↓
   🃏 WSTAWIANIE
```

```text
środek + lewy + prawy
        ↓
   ⚡ BINARNE
```

```text
a % b + zamiana a,b
        ↓
   🔢 EUKLIDES
```

```text
pivot
        ↓
   ⚡ QUICKSORT
```

```text
podziel + scal
        ↓
   🔀 MERGE SORT
```

```text
funkcja wywołuje samą siebie
        ↓
   🔄 REKURENCJA
```

```text
n % i == 0
        ↓
   🔍 DZIELNIKI / PIERWSZA
```

```text
licznik += 1
        ↓
   🔢 ZLICZANIE
```

---

# ⭐ Co naprawdę zapamiętać

Na początek **nie ucz się tych algorytmów na pamięć linijka po linijce**. Naucz się rozpoznawać ich „odcisk palca”:

**Bąbelkowe** → sąsiedzi
**Wybieranie** → minimum/maksimum
**Wstawianie** → przesuwanie + wstawianie
**Binarne** → środek
**Euklides** → `%`
**Pierwsza** → sprawdzanie dzielników
**Quicksort** → pivot
**Merge sort** → podział + scalanie
**Rekurencja** → funkcja wywołuje siebie
**Zliczanie** → licznik `+= 1`

Jeżeli opanujesz te skojarzenia, **dużo zadań z algorytmów będziesz w stanie rozpoznać bez odpalania Pythona**.
