
def pos_negativa(a,b,negativa):
    if negativa:
        if a < 0 and b < 0:
            return True
        else:
            return False
    if not negativa:
        if a > 0 and b < 0:
            return True
        elif a < 0 and b > 0:
            return True
        else:
            return False


num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un segundo número: "))
negativa_input = str(input("True or False? "))
if negativa_input == "True":
    negativa_input = True
elif negativa_input == "False":
    negativa_input = False
print(pos_negativa(num1, num2, negativa_input))
