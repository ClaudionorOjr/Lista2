def questao1():
    return (5 ** 2, 9 * 5, 15 / 12, 12 / 15, 15 // 12, 12 // 15, 5 % 2, 9 % 5, 15 % 12, 12 % 15, 6 % 6, 0 % 7)


def questao2():      
    a = 51           
    a//24
    resto1 = a%24
    alarme = 2 + resto1
    return print(alarme,"horas da tarde")

def questao3():
    a = int(input("Hora atual:"))
    b = int(input("Horas de espera até o alarme tocar:"))
    b//24
    resto1 = b%24

    alarme = a + resto1
    return print(alarme,"horas")

from datetime import date
def questao4(a,c):
    a = date.today()
    futuro = date.fromordinal(a.toordinal()+c)
    dias = ("segunda-feira","terça-feira","quarta-feira","quinta-feira","sexta-feira","sábado","domingo")
    return dias[futuro.weekday()]

def questao5():
    a = str("Só")
    b = str("trabalho")
    c = str("sem")
    d = str("diversão")
    e = str("faz")
    f = str("de")
    g = str("João")
    h = str("em")
    i = str("chato")
    return print(a,b,c,d,e,f,g,h,i)

def questao6(a,b,c):  
    x = a*(b-c)       
    return x

def questao7(t):      
    a = 10000*((1+0.08/12)**(12*t))
    return a

def questao8(r):      
    area = 3.14*(r**2)
    return area

def questao9(a,b):    
    area = a*b
    return area

def questao10(km,l):   
    consumo = km/l
    return consumo

def questao11(c):      
    f = (c*1.8)+32
    return f

def questao12(f):      
    c = (f-32)/1.8
    return c















