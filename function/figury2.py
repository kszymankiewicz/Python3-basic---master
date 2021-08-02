import figury1
from enum import IntEnum

Menu_Figury = IntEnum('Menu_Figury', 'Kwadrat Prostokąt Koło Trójkąt Trapez')

choice = int(input(""" Wybierz figurę, której pole chcesz obliczyć :
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez   
"""))

if (choice == Menu_Figury.Kwadrat):
    a = float(input('Podaj bok kwadratu:'))
    print('Pole kwadratu wynosi: ', figury1.pole_kwadratu(a))
elif (choice == Menu_Figury.Prostokąt):
    a = float(input('Podaj pierwszy bok prostokąta:'))
    b = float(input('Podaj drugi bok prostokąta:'))
    print('Pole prostokąta wynosi: ', figury1.pole_prostokata(a,b))
elif (choice == Menu_Figury.Koło):
    r = float(input('Podaj promień koła: '))
    print('Pole koła wynosi: ', figury1.pole_kola(r))
elif (choice == Menu_Figury.Trójkąt):
    a = float(input('Podaj długość podstawy tójkąta: '))
    h = float(input('Podaj wysokość trójkąta:'))
    print('Pole trójkąta wynosi: ', figury1.pole_trojkata(a,h)) 
elif (choice == Menu_Figury.Trapez):
    a = float(input('Podaj długość pierwszej podstawy : '))
    b = float(input('Podaj długość drugiej podstawy:'))
    h = float(input('Podaj wysokość trapezu:'))
    print('Pole trapezu wynosi: ', figury1.pole_trapezu(a,b,h)) 
