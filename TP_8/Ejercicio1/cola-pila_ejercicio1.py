from queue import Cola
from constants import *
from plane import Plane
from time import sleep


class TorreDeControl(Cola):
    def recognition(self):
        checking = str(input(INPUT_RECOGNITION))
        if checking == "Y":
            model = str(input("Enter aircraft model: "))
            flight = int(input("Enter flight number: "))
            waiting = str(input("Waiting for [land] or [take off]: "))
            plane = Plane(model, flight, waiting)
            self.push(plane)
        else:
            pass

    def action(self):
        checking = str(input(INPUT_ACTION))
        if checking == "Y":
            plane = self.pop()
            print("All right, flight number %s is going to %s. It was removed from the queue." % (plane.flight, plane.waiting_for))
        else:
            pass

    def status(self):
        print("QUEUE OF WAITING PLANES")
        queue = self.get_elements()
        if queue:
            for element in queue:
                print(element)
        else:
            print("The queue is empty")


mi_torre = TorreDeControl()
print(CONNECTING)
sleep(3)

while True:
    print(MAIN_MENU)
    choice = int(input(INPUT_MAIN_MENU))
    if choice == 1:
        mi_torre.recognition()
        print(RETURNING)
        sleep(3)
    if choice == 2:
        mi_torre.action()
        print(RETURNING)
        sleep(3)
    if choice == 3:
        mi_torre.status()
        print(RETURNING)
        sleep(3)
    if choice == 4:
        print(DISCONNECTING)
        sleep(3)
        break
    else:
        print("Input error. Try again.")
        print(RETURNING)
        sleep(3)

