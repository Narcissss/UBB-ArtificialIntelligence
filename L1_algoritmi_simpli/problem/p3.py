"""
Să se determine produsul scalar a doi vectori rari care conțin numere reale. Un vector este rar
atunci când conține multe elemente nule.
De ex. produsul scalar dintre [1,0,2,0,3] și [1,2,0,3,1] este 4.

Complexitate: O(n) - timp, O(1) - spatiu suplimentar
"""

from typing import Tuple
from problem.utils import getAbsolutePath


def readVectors(path: str) -> Tuple[list, list]:
    vectors = ([], [])
    with open(path, 'r') as fileD:
        lines = fileD.readlines()
        for number in lines[0].split():
            vectors[0].append(float(number))
        for number in lines[1].split():
            vectors[1].append(float(number))
    return vectors

def getDotProduct(vectors: Tuple[list, list]) -> float:
    dotProduct = 0
    for x, y in zip(vectors[0], vectors[1]):
        dotProduct += x * y
    return dotProduct

def test_getDotProduct():
    path = getAbsolutePath(__file__, "../data/p3.txt")
    vectors = readVectors(path)
    dotProduct = getDotProduct(vectors)
    assert(dotProduct == 4)
    print("P3: " + str(dotProduct)) # TODO: delete

def runTests():
    test_getDotProduct()
