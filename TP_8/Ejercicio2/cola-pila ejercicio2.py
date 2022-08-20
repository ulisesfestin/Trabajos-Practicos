from queue import Cola
from constants import *
from time import sleep


class ColaDePacientes(Cola):
    def new_patient(self, new):
        self.push(new)

    def next_patient(self):
        next = self.pop()
        return next


my_consulting_room = ColaDePacientes()
print(CONNECTING)
sleep(3)

while True:
    print(MAIN_MENU)
    choice = int(input(INPUT_MAIN_MENU))
    if choice == 1:
        name = str(input("Enter the patient's name: "))
        my_consulting_room.new_patient(name)
        print(RETURNING)
        sleep(3)
    elif choice == 2:
        patient = my_consulting_room.next_patient()
        if patient:
            print("Next patient: %s" % patient)
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
