#variables
print('Calculadora python, v;2.0 funcional')
x = int(input ("Escribe la primera variable: "))
y = int(input ("Escribe la segunda variable: "))
list = ['sumar = s' , 'restar = r' , 'multiplicar = m' , 'dividir = d']
print(list)
z = input ("Escribe segun la anterior lista: ")

#codigo
if z == 's' :
    while True:
        print(x+y)

if z == "r" :
    while True:
        print(x-y)

if z == "m":
    while True:
        print(x*y)

if z == "d" :
    while True:
        print(x/y)


