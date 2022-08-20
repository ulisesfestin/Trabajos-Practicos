class Pila:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            print("No hay elementos")

    def peek(self):
        return self.elements[-1]

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def get_elements(self):
        return self.elements
