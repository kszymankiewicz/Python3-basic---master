"""
break

continue
"""

wynik = 0

i = 0

while i < 3:
    x = int(input("Podaj dodatnią liczbę:"))
    if (x > 0):
        wynik += x
    else:
        print("Miała być liczba dodatnia, zapytam się o liczbę dodatnią ponownie")
        continue
    print("Aktualny wynik dodawania to:", wynik)
    i += 1


