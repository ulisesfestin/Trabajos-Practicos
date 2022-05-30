def problemas_monos(a_sonriendo, b_sonriendo):
    if a_sonriendo and b_sonriendo:
        return True
    elif not a_sonriendo and not b_sonriendo:
        return True
    elif a_sonriendo and not b_sonriendo:
        return False
    else:
        return False


mono_a = str(input("¿Está sonriendo el mono A? "))
if mono_a == "si":
    mono_a = True
else:
    mono_a = False
mono_b = str(input("¿Está sonriendo el mono B? "))
if mono_b == "si":
    mono_b = True
else:
    mono_b = False

print(problemas_monos(mono_a,mono_b))
