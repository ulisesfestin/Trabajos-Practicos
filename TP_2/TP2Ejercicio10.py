# Ejercicio 10. Escribir un programa, que reciba una expresión y un archivo e imprima las líneas del archivo que
# contienen la expresión recibida.

class File:
    def __init__(self, directory):
        self.directory = directory

    def print_lines(self):
        f = open(self.directory, "r")
        word = str(input("Enter a expression: "))
        print("These lines contain that expression:")
        for line in f:
            if word in line:
                print(line.replace("\n", ""))
        f.close()
        return


example_text = File("example3.txt")
example_text.print_lines()
