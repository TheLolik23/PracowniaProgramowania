from operator import index

# Import 'index' jest zbędny dla obecnego kodu, ponieważ nie jest używany.

# Zad 2.1
# Otwarcie pliku 'symbole_przyklad.txt' w trybie odczytu ('r')
plik = open('Assets/Data/Maj_2025/symbole_przyklad.txt', 'r')
# Wczytanie zawartości pliku. 'plik.read()' czyta całość jako jeden ciąg.
# 'splitlines()' dzieli ciąg na listę wierszy (linii), usuwając znaki nowej linii.
data = plik.read().splitlines()

# Iteracja po każdym wierszu (ciągu znaków) wczytanym z pliku
for line in data:
    # Odwrócenie bieżącego wiersza. line[::-1] tworzy nową listę/ciąg
    # zaczynając od końca do początku, z krokiem -1.
    reversed_line = line[::-1]

    # Sprawdzenie, czy odwrócony wiersz jest identyczny z oryginalnym,
    # co oznacza, że wiersz jest palindromem.
    if reversed_line == line:
        # Jeśli jest palindromem, wypisz go na konsolę
        print(line)



# Zad 2.2
# Inicjalizacja listy do przechowywania współrzędnych środka znalezionych kwadratów 3x3
kwadraty = []
# Zmienna przechowująca stałą szerokość wierszy danych.
# Zakładamy, że wszystkie wiersze mają tę samą długość (12 znaków, jak w danych przykładowych).
liczba_znakow = 12

# Pętla iteruje po indeksach wierszy, które mogą być górną krawędzią kwadratu 3x3.
# Zatrzymuje się na 3. wierszu od końca (len(data) - 3),
# aby zagwarantować, że są dostępne jeszcze dwa wiersze poniżej (i+1, i+2).
for i in range(len(data) - 2):
    # Pętla iteruje po indeksach kolumn, które mogą być lewą krawędzią kwadratu 3x3.
    # Zatrzymuje się na 3. kolumnie od końca (liczba_znakow - 3),
    # aby zagwarantować, że są dostępne jeszcze dwie kolumny z prawej (j+1, j+2).
    for j in range(liczba_znakow - 2):

        # Przypisanie referencji do trzech kolejnych wierszy,
        # rozpoczynając od wiersza o indeksie 'i'.
        wiersz1 = data[i]
        wiersz2 = data[i + 1]
        wiersz3 = data[i + 2]

        # Wyodrębnienie trzech kolejnych znaków z każdego z trzech wierszy,
        # rozpoczynając od kolumny o indeksie 'j'.
        znaki1 = wiersz1[j] + wiersz1[j + 1] + wiersz1[j + 2]
        znaki2 = wiersz2[j] + wiersz2[j + 1] + wiersz2[j + 2]
        znaki3 = wiersz3[j] + wiersz3[j + 1] + wiersz3[j + 2]

        # Sprawdzenie, czy wszystkie 3 znaki w pierwszym wierszu (znaki1) są takie same.
        # Jest to pierwszy warunek na kwadrat 3x3 (identyczne symbole w całym kwadracie).
        czy_znaki = (znaki1[0] == znaki1[1] == znaki1[2])

        # Sprawdzenie, czy sekwencje 3 znaków w wierszach (znaki1, znaki2, znaki3)
        # są identyczne. Oznacza to, że drugi i trzeci wiersz mają
        # ten sam ciąg 3 znaków, co pierwszy wiersz.
        # Jest to drugi warunek na kwadrat 3x3.
        czy_trojki = (znaki1 == znaki2 == znaki3)

        # Jeśli oba warunki są spełnione, oznacza to, że znaleziono kwadrat 3x3,
        # złożony z identycznych symboli.
        if czy_znaki and czy_trojki:
            # Dodanie współrzędnych środka znalezionego kwadratu do listy.
            # Współrzędne (indeks wiersza, indeks kolumny) środka kwadratu 3x3
            # są przesunięte o +1 w stosunku do jego lewego górnego rogu (i, j).
            # Ponieważ indeksowanie w pliku zaczyna się od 1 (jak w treści zadania maturalnego),
            # dodajemy 1 do indeksu i (wiersza) i j (kolumny), a następnie jeszcze 1
            # (czyli łącznie +2) by wskazać środek.
            # i+2 to indeks wiersza środkowego, j+2 to indeks kolumny środkowej.
            kwadraty.append((i + 2, j + 2))

# Wypisanie całkowitej liczby znalezionych kwadratów.
print("Liczba kwadratów: ", len(kwadraty))

# Wypisanie współrzędnych środka (wiersz, kolumna) każdego znalezionego kwadratu.
# Wiersz i kolumna są podane z indeksowaniem od 1.
for wiersz, kolumna in kwadraty:
    print(wiersz, kolumna)



# Zad 2.3
# Inicjalizacja zmiennej do przechowywania największej wartości dziesiętnej
# uzyskanej z konwersji wiersza trójkowego.
max_wartosc = 0
# Inicjalizacja zmiennej do przechowywania wiersza-symbole, który odpowiada największej wartości.
max_liczba_symbole = ""

# Iteracja po każdym wierszu z danych.
for line in data:

    # Inicjalizacja pustego ciągu do przechowywania cyfr trójkowych ('0', '1', '2')
    # odpowiadających symbolom w bieżącym wierszu.
    obecna_liczba_trojkowa = ""

    # Przejście przez każdy symbol w bieżącym wierszu.
    for letter in line:
        # Konwersja symbolu na odpowiadającą mu cyfrę w systemie trójkowym:
        if letter == 'o':
            obecna_liczba_trojkowa += '0'  # 'o' -> 0
        elif letter == '+':
            obecna_liczba_trojkowa += '1'  # '+' -> 1
        elif letter == '*':
            obecna_liczba_trojkowa += '2'  # '*' -> 2

    # Konwersja ciągu cyfr trójkowych na liczbę w systemie dziesiętnym (int(ciąg, podstawa)).
    wartosc_dziesietna = int(obecna_liczba_trojkowa, 3)

    # Sprawdzenie, czy uzyskana wartość jest większa niż dotychczasowe maksimum.
    if wartosc_dziesietna > max_wartosc:
        # Jeśli tak, aktualizacja maksimum.
        max_wartosc = wartosc_dziesietna
        # Zapamiętanie oryginalnego wiersza symboli, który dał tę wartość.
        max_liczba_symbole = line

# Wypisanie największej wartości dziesiętnej i odpowiadającego jej wiersza symboli.
print(max_wartosc, max_liczba_symbole)



# Zad 2.4
# Inicjalizacja zmiennej do przechowywania sumy wszystkich wartości dziesiętnych.
suma_dziesietna = 0

# Sekwencja konwersji i sumowania jest identyczna jak w Zad 2.3,
# z tą różnicą, że zamiast szukać maksimum, sumujemy wszystkie wartości.

# Iteracja po każdym wierszu z danych.
for line in data:

    # Inicjalizacja pustego ciągu na cyfry trójkowe.
    obecna_liczba_trojkowa = ""

    # Konwersja symboli na ciąg cyfr trójkowych ('0', '1', '2').
    for letter in line:
        if letter == 'o':
            obecna_liczba_trojkowa += '0'
        elif letter == '+':
            obecna_liczba_trojkowa += '1'
        elif letter == '*':
            obecna_liczba_trojkowa += '2'

    # Konwersja ciągu cyfr trójkowych na liczbę w systemie dziesiętnym.
    wartosc_dziesietna = int(obecna_liczba_trojkowa, 3)

    # Dodanie uzyskanej wartości dziesiętnej do sumy.
    suma_dziesietna += wartosc_dziesietna

# Konwersja sumy dziesiętnej z powrotem na postać trójkową.
# Inicjalizacja pustego ciągu na wynik w systemie trójkowym.
zapis_trojkowy = ''
# Utworzenie kopii sumy, ponieważ oryginalna wartość jest modyfikowana w pętli.
kopia_sumy = suma_dziesietna

# Algorytm konwersji z systemu dziesiętnego na trójkowy poprzez wielokrotne
# dzielenie całkowite przez 3 i branie reszt z dzielenia.
while kopia_sumy > 0:
    # Reszta z dzielenia przez 3 to kolejna (od prawej) cyfra trójkowa.
    # Jest ona dodawana na początek ciągu 'zapis_trojkowy'.
    zapis_trojkowy = str(kopia_sumy % 3) + zapis_trojkowy
    # Dzielenie całkowite liczby przez 3, aby przejść do kolejnej cyfry.
    kopia_sumy //= 3

# Konwersja ciągu cyfr trójkowych ('0', '1', '2') na ciąg symboli ('o', '+', '*').
symbole_sumy = ''
for k in zapis_trojkowy:
    if k == '0':
        symbole_sumy += 'o'  # 0 -> 'o'
    elif k == '1':
        symbole_sumy += '+'  # 1 -> '+'
    elif k == '2':
        symbole_sumy += '*'  # 2 -> '*'

# Wypisanie sumy dziesiętnej oraz jej zapisu w postaci symboli (system trójkowy).
print(suma_dziesietna, symbole_sumy)

# Zamknięcie pliku po zakończeniu wszystkich operacji.
plik.close()