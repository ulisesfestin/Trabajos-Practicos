

def suma_doble(a,b):
    if a != b:
        c = a + b
        return c
    elif a == b:
        c = (a + b) * 2
        return c


num1 = int(input("Ingrese un entero: "))
num2 = int(input("Ingrese otro entero: "))
resultado = suma_doble(num1, num2)
print("El resultado es: ", resultado)
