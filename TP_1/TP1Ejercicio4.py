num = int(input("Ingrese un número entero: "))

def diferencia21(n):
    if n <= 21:
        diferencia = 21 - n
        return diferencia
    if n > 21:
        diferencia = (n - 21) * 2
        return diferencia

print(diferencia21(num))
