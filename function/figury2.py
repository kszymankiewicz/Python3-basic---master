import figury

choice = input(""" Wybierz figurę, której pole chcesz obliczyć :
1. Kwadrat
2. Prostokąt
3. Koło
4. Trójkąt
5. Trapez   
""")

if (choice == '1'):
    a = float(input('Podaj bok kwadratu:'))
    print('Pole kwadratu wynosi: '+ str(figury.pole_kwadratu(a)))
elif (choice == '2'):
    a = float(input('Podaj pierwszy bok prostokąta:'))
    b = float(input('Podaj drugi bok prostokąta:'))
    print('Pole prostokąta wynosi: '+ str(figury.pole_prostokata(a,b)))
elif (choice == '3'):
    r = float(input('Podaj promień koła: '))
    print('Pole koła wynosi: '+ str(figury.pole_kola(r)))
elif (choice == '4'):
    a = float(input('Podaj długość podstawy tójkąta: '))
    h = float(input('Podaj wysokość trójkąta:'))
    print('Pole trójkąta wynosi: '+ str(figury.pole_trojkata(a,h))) 
elif (choice == '5'):
    a = float(input('Podaj długość pierwszej podstawy : '))
    b = float(input('Podaj długośćć drugij podstawy:'))
    h = float(input('Podaj wysokość trapezu:'))
    print('Pole trapezu wynosi: '+ str(figury.pole_trapezu(a,b,h))) 
