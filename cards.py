from functional import seq
import random

symbols = ["Heart", "Spade", "Diamond", "Clover"]
points = [
    {"num":"A","point":11}, 
    {"num":"K","point":10},
    {"num":"Q","point":10},
    {"num":"J","point":10},
    {"num":"10","point":10},
    {"num":"9","point":9},
    {"num":"8","point":8},
    {"num":"7","point":7},
    {"num":"6","point":6},
    {"num":"5","point":5},
    {"num":"4","point":4},
    {"num":"3","point":3},
    {"num":"2","point":2},
]


def addSymbols(symbol):
    return seq(points).map(lambda point: {**point, "symbol": symbol})

cards = seq(symbols).map(addSymbols).flatten().to_list()
random.shuffle(cards)
