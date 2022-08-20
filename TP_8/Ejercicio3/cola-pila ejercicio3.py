from pila import Pila
from constants import *
from time import sleep


class Carta:
    def __init__(self, value, palo):
        self.palo = palo
        self.valor = value

    def __str__(self):
        string = str(self.valor) + " de " + self.palo
        return string


class PilaDeCartas(Pila):
    def apilar(self, carta):
        if self.elements:
            if carta.valor == (self.peek().valor - 1) and carta.palo != self.peek().palo:
                self.push(carta)
            else:
                print("Error, sólo se permite apilarla si es de un número inmediatamente inferior y de distinto palo a la anterior.")
        else:
            self.push(carta)

    def mostrar_pila(self):
        for element in self.elements:
            print(element)


my_pila_de_cartas = PilaDeCartas()
print(CONNECTING)
sleep(3)


while True:
    print(MAIN_MENU)
    choice = int(input(INPUT_MAIN_MENU))
    if choice == 1:
        valor = int(input("Ingrese valor de la carta (del 1 al 12): "))
        palo = str(input("Ingrese palo de la carta (oro, copas, basto, espada): "))
        carta = Carta(valor, palo)
        my_pila_de_cartas.apilar(carta)
        print(RETURNING)
        sleep(3)
    elif choice == 2:
        my_pila_de_cartas.mostrar_pila()
        print(RETURNING)
        sleep(3)
    elif choice == 3:
        print(DISCONNECTING)
        sleep(3)
        break
    else:
        print("Input error. Try Again")
        print(RETURNING)
        sleep(3)
