dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]


def dormimos(dia_semana, vacaciones):
    if not dia_semana and not vacaciones:
        dormir = True
        return dormir
    elif dia_semana and not vacaciones:
        dormir = False
        return dormir
    elif not dia_semana and vacaciones:
        dormir = True
        return dormir
    else:
        dormir = True
        return dormir


dia = str(input("Ingrese el día: "))
if dia in dias_semana:
    dia = True
else:
    dia = False

vacaciones = str(input("¿Estás de vacaciones? "))
if vacaciones == "si":
    vacaciones = True
else:
    vacaciones = False

print(dia,vacaciones)
a = dormimos(dia,vacaciones)
print(a)
