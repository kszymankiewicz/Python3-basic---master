import math

def pole_kwadratu(a):
    return a * a   

def pole_prostokata(a, b):
    return a * b   

def pole_kola(r):
    return math.pi * r ** 2
    
def pole_trojkata(a, h):
    return 0.5 * a * h
    
def pole_trapezu(a, b, h):
    return (a + b) / 2 * h
    
    
print('Pole koła wynosie: ' +str(pole_kola(2)))
print('Pole kwadratu wynosie: ' + str(pole_kwadratu(3)))
print('Pole trójkąta wynosie: ' + str(pole_trojkata(4,5)))
print('Pole prostokąta wynosie: ' + str(pole_prostokata(3,4)))
print('Pole trapezu wynosie: ' + str(pole_trapezu(2,2,3)))
