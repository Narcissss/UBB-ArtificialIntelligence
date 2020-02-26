"""
 Considerându-se o matrice cu n x m elemente binare (0 sau 1), să se înlocuiască cu 1 toate
aparițiile elementelor egale cu 0 care sunt complet înconjurate de 1.
De ex. matricea
[[1,1,1,1,0,0,1,1,0,1],
 [1,0,0,1,1,0,1,1,1,1],
 [1,0,0,1,1,1,1,1,1,1],
 [1,1,1,1,0,0,1,1,0,1],
 [1,0,0,1,1,0,1,1,0,0],
 [1,1,0,1,1,0,0,1,0,1],
 [1,1,1,0,1,0,1,0,0,1],
 [1,1,1,0,1,1,1,1,1,1]]
devine
[[1,1,1,1,0,0,1,1,0,1],
 [1,1,1,1,1,0,1,1,1,1],
 [1,1,1,1,1,1,1,1,1,1],
 [1,1,1,1,1,1,1,1,0,1],
 [1,1,1,1,1,1,1,1,0,0],
 [1,1,1,1,1,1,1,1,0,1],
 [1,1,1,0,1,1,1,0,0,1],
 [1,1,1,0,1,1,1,1,1,1]]

 Complexitate: O(n*m) - timp, O(1) - spatiu suplimentar
"""

from problem.utils import getAbsolutePath
from typing import List
import unittest


def readMatrix(path: str) -> List[List[int]]:
    matrix = []
    with open(path, "r") as fileD:
        for line in fileD.readlines():
            matrix.append([int(number) for number in line.split(',')])
    return matrix

def fill(matrix: List[List[int]], i: int, j: int, rows: int, cols: int) -> None:
    matrix[i][j] = 2
    if i > 0 and matrix[i - 1][j] == 0:
        fill(matrix, i - 1, j, rows, cols)
    if i + 1 < rows and matrix[i + 1][j] == 0:
        fill(matrix, i + 1, j, rows, cols)
    if j > 0 and matrix[i][j - 1] == 0:
        fill(matrix, i, j - 1, rows, cols)
    if j + 1 < cols and matrix[i][j + 1] == 0:
        fill(matrix, i, j + 1, rows, cols)

def setMatrixValues(matrix: List[List[int]], n: int, m: int):
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2: matrix[i][j] = 0
            elif matrix[i][j] == 0: matrix[i][j] = 1

def fiilInCenter(matrix: List[List[int]]):
    n = len(matrix)
    m = len(matrix[0])

    for rowIdx in range(n):
        if matrix[rowIdx][0] == 0:
            fill(matrix, rowIdx, 0, n, m)
        if matrix[rowIdx][m-1] == 0:
            fill(matrix, rowIdx, m - 1, n, m)
    for colIdx in range(m):
        if matrix[0][colIdx] == 0:
            fill(matrix, 0, colIdx, n, m)
        if matrix[n-1][colIdx] == 0:
            fill(matrix, n - 1, colIdx, n, m)

    setMatrixValues(matrix, n, m)
    return None

def test_fillInCenter():
    path = getAbsolutePath(__file__, "../data/p11.txt")
    
    matrix = readMatrix(path)
    fiilInCenter(matrix)

    expected = [[1,1,1,1,0,0,1,1,0,1], [1,1,1,1,1,0,1,1,1,1],
                 [1,1,1,1,1,1,1,1,1,1], [1,1,1,1,1,1,1,1,0,1], 
                 [1,1,1,1,1,1,1,1,0,0], [1,1,1,1,1,1,1,1,0,1], 
                 [1,1,1,0,1,1,1,0,0,1], [1,1,1,0,1,1,1,1,1,1]]
    
    assert(matrix == expected)
    print("P11: " + str(matrix)) # TODO: delete

def runTests():
    test_fillInCenter()

