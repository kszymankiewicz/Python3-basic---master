"""
INSTRUKCJA WARUNKOWA

JESLI (PRAWDA)
 TO...
JESLI CO INNEGO (PRAWDA)
 TO...
A CALKOWICIE W INNYM WYPADKU
 TO...

 elif od ang else if

"""
wybor = input("* - mnożenie, / - dzielić, + - dodawać, - - odejmować: ")

a = int(input("Pierwsza liczba: "))
b = int(input("Druga liczba: "))

if (wybor == '*'):
    print(a * b)
elif (wybor == '/'):
    if (b == 0):
        print("Cholero nie dziel przez zero")
    else:   
        print(a / b)
elif (wybor == '+'):
    print(a + b)
elif (wybor == '-'):
    print(a - b)
else:
    print("nie wybrałeś dobrego wyboru")




