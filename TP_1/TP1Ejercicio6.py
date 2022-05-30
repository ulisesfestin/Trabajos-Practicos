num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

def hacer10(a,b):
    if a == 10 or b == 10:
        return True
    elif a + b == 10:
        return True
    else:
        return False


print(hacer10(num1,num2))