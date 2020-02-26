"""
Considerându-se o matrice cu n x m elemente întregi și coordonatele a 2 căsuțe din matrice
((p,q) și (r,s)), să se calculeze suma elementelor din sub-matricea identificată de cele 2
căsuțe.
De ex, pt matricea
[[0, 2, 5, 4, 1],
 [4, 8, 2, 3, 7],
 [6, 3, 4, 6, 2],
 [7, 3, 1, 8, 3],
 [1, 5, 7, 9, 4]]
și căsuțele de coordinate (1, 1) și (3, 3) suma elementelor din sub-matrice este 38. 

Complexitate: O(n*m) - timp, O(1) - spatiu suplimentar
    n, m -> dimensiunile matricii
"""

from problem.utils import getAbsolutePath
from typing import List, Tuple

def readMatrix(path: str) -> Tuple[List[List[int]], Tuple[int, int], Tuple[int, int]]:
    matrix = []
    with open(path, "r") as fileD:
        line = fileD.readline()
        n = int(line[0])
        for i in range(n):
            line = fileD.readline()
            matrix.append([int(number) for number in line.split()])
        line = fileD.readline().split()
        x1, y1 = line[0], line[1]
        line = fileD.readline().split()
        x2, y2 = line[0], line[1]
        return (matrix, (int(x1), int(y1)), (int(x2), int(y2)))

def calculateSum(matrix: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]) -> int:
    sum = 0
    for i in range(start[0], end[0] + 1):
        for j in range(start[1], end[1] + 1):
            sum += matrix[i][j]
    return sum

def test_calculateSum():
    path = getAbsolutePath(__file__, "../data/p9.txt")
    data = readMatrix(path)
    submatrixSum = calculateSum(data[0], data[1], data[2])
    assert(submatrixSum == 38)
    print("P9: " + str(submatrixSum)) # TODO: delete

def runTests():
    test_calculateSum()


