# Ejercicio 5. Escribir un programa, para copiar el contenido de un archivo a otro archivo.

class archive:
    def __init__(self, directory1, directory2):
        self.original_text = directory1
        self.copy_text = directory2

    def copy_to_other_file(self):
        text1 = open(self.original_text, "r")
        text2 = open(self.copy_text, "w")
        for line in text1:
            text2.write(line)
        text1.close()
        text2.close()


book = archive("example.txt", "example2.txt")
book.copy_to_other_file()

