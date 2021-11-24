import random


def sucesos(prob=0.5):
    while True:
        yield random.random() < prob
