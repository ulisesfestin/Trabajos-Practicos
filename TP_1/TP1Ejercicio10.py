string = str(input("Ingrese una palabra: "))
num = int(input("Ingrese un entero: "))


def caracter_perdido(str, n):
    new_string = ""
    if 0 <= n <= (len(str)-1):
        for i in range(len(str)):
            if i != n:
                new_string = new_string + str[i]
            else:
                pass
        return new_string
    else:
        return "El índice no se encuentra en el rango."


print(caracter_perdido(string, num))
