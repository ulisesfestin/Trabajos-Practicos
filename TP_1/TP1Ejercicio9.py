palabra = str(input("Ingrese una cadena de caracteres: "))

def no_cadena(string):
    if string[0] == "n" and string[1] == "o":
        return string
    else:
        string = "no " + string
        return string


print(no_cadena(palabra))
