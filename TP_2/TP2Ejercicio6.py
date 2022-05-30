# Ejercicio 6. Escribir un programa, que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

class text:
    def __init__(self, directory):
        self.directory = directory

    def read_file(self, n):
        file = open(self.directory, "r")
        for i in range(n):
            line = file.readline()
            print(line.replace("\n", ""))
        return


example_text = text("example.txt")
n_lines = int(input("Enter number of lines to read: "))
print("Text:")
example_text.read_file(n_lines)
