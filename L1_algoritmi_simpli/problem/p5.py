"""
Pentru un șir cu n elemente care conține valori din mulțimea {1, 2, ..., n - 1} astfel încât o
valaore se repetă de două ori, să se identifice acea valoare care se repetă.
De ex. în șirul [1,2,3,4,2] valoarea 2 apare de două ori.

Complexitate: O(n) - timp, O(1) - spatiu suplimentar
"""

from typing import List

def findDuplicateNumber(numberList: List[int], interval: int) -> int:
    sum = 0
    i = 0
    for number in numberList:
        sum += number
        sum -= i
        i += 1
    return sum

def test_findDuplicateNumber():
    numberList = [1, 2, 3, 4, 2]
    duplicateNumber = findDuplicateNumber(numberList, 4)
    assert(duplicateNumber == 2)
    print("P5: " + str(duplicateNumber)) # TODO: delete

def runTests():
    test_findDuplicateNumber()
