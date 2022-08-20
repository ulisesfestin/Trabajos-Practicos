class Cola:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.insert(0, element)

    def pop(self):
        try:
            return self.elements.pop()
        except IndexError:
            print("There are no elements.")

    def size(self):
        return len(self.elements)

    def is_empty(self):
        return self.elements == []

    def get_elements(self):
        return self.elements
