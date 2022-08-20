class Plane:
    def __init__(self, model, flight, waiting):
        self.model = model
        self.flight = flight
        self.waiting_for = waiting

    def __str__(self):
        string = "Model: %s || Flight number: %s" % (self.model, self.flight)
        return string
