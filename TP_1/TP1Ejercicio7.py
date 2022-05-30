num = int(input("Ingrese un número: "))


def cerca_cien(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


print(cerca_cien(num))
