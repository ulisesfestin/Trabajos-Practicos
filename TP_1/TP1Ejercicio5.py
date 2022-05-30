hablando = str(input("¿El loro está hablando? "))
hora = int(input("¿Qué hora es? "))

def problema_loro(a,b):
    if a == "si" and 7 > b < 20:
        return True
    else:
        return False

print(problema_loro(hablando,hora))
