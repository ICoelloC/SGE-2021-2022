from tiranosaurio import Rex
from spinosaurio import Spinosaurio
from triceratops import Triceraptops
from yacimiento import Yacimiento
import random


class FactroriaYacimiento:

    def crear_mundo(self, num_rex, num_spinosaurus, num_triceraptors):
        a = Yacimiento(self)
        for i in range(num_rex):
            a.add_dinosaurio(Rex("T-Rex #" + str(i), 1000, random.randrange(-200, 200), a))
        for i in range(num_spinosaurus):
            a.add_dinosaurio(Spinosaurio("Spinosaurio #" + str(i), 1000, random.randrange(-200, 200), a))
        for i in range(num_triceraptors):
            a.add_dinosaurio(Triceraptops("Triceratops #" + str(i), 1000, random.randrange(-200, 200), a))
        return a
