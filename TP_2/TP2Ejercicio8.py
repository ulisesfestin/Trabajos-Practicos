# Ejercicio 8. Escribir un programa, que dado un archivo de texto, un delimitador, y una lista de campos, imprima
# solamente esos campos, separados por ese delimitador.

class read_txt_file:
    def __init__(self, directory, separator):
        self.directory = directory
        self.separator = separator

    def read_text(self):
        self.separator = input("Enter the separator: ")
        f = open(self.directory, "r")
        read_file = f.readlines()
        new_string = ' '.join(read_file)
        my_list = new_string.split(" ")
        new_string1 = self.separator.join(my_list)
        print(new_string1)


text_example = read_txt_file("example.txt", " ")
print(text_example.read_text())
