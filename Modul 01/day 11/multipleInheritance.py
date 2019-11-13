class Karnivora:
    def __init__(self):
        self.daging = True

class Herbivora:
    def __init__(self):
        self.tumbuhan = True

class Omnivora(Karnivora, Herbivora):
    def __init__(self):
        Karnivora.__init__(self)
        Herbivora.__init__(self)
        self.mcD = True

objectA = Omnivora()
print(vars(objectA))