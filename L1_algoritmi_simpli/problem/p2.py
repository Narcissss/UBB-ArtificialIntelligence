"""
Să se determine distanța Euclideană între două locații identificate prin perechi de numere.
De ex. distanța între (1,5) și (4,1) este 5.0

Complexitate: O(1) - timp, O(1) - spatiu suplimentar
"""
from typing import List
import math
from problem.utils import getAbsolutePath


def readNumbers(path: str) -> List[tuple]:
    coords = []
    with open(path, "r") as fileD:
        for line in fileD:
            numbers = line.split()
            point = (float(numbers[0]), float(numbers[1]))
            coords.append(point)
    return coords

def getEuclDist(coords: List[tuple]) -> float:
    sum = 0
    for point in coords:
        sum += (point[0] - point[1])**2
    return math.sqrt(sum)

def test_getEuclDist():
    path = getAbsolutePath(__file__, "../data/p2.txt")
    coords = readNumbers(path)
    euclDist = getEuclDist(coords)
    assert(euclDist == 5)
    print("P2: " + str(euclDist)) # TODO: delete

def runTests():
    test_getEuclDist()
