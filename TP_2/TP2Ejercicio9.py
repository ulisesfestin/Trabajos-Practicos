# Ejercicio 9. Escribir un programa, que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas
# palabras y cuántos caracteres contiene el archivo.

class file:
    def __init__(self, directory):
        self.directory = directory

    def number_of_words(self):
        f = open(self.directory, "r")
        read = f.read()
        words = read.split()
        f.close()
        return len(words)

    def number_of_letters(self):
        f = open(self.directory, "r")
        characters = 0
        lines = 1
        for line in f:
            characters += len(line)
            if line == "\n":
                characters += 1
                lines += 1
        f.close()
        return characters

    def number_of_lines(self):
        f = open(self.directory, "r")
        characters = 0
        lines = 0
        for line in f:
            characters += len(line)
            lines += 1
            if line == "\n":
                characters += 1
        f.close()
        return lines


example_text = file("example3.txt")
print("This text have:")
print("Number of words:", example_text.number_of_words())
print("Number of characters:", example_text.number_of_letters())
print("Number of lines:", example_text.number_of_lines())
