"""
Pentru un șir cu n numere întregi care conține și duplicate, să se determine elementul
majoritar (care apare de mai mult de n / 2 ori).
De ex. 2 este elementul majoritar în șirul [2,8,7,2,2,5,2,3,1,2,2].

Complexitate: O(n * log(n)) - timp, O(1) - spatiu suplimentar
"""

from typing import List

def findMajorityNumber(lst: List[int]) -> int:
    mid = len(lst) // 2
    lst.sort()
    number = lst[mid]
    return number

def test_findMajorityNumber():
    lst = [2,8,7,2,2,5,2,3,1,2,2]
    majNumber = findMajorityNumber(lst)
    assert(majNumber == 2)
    print("P6: " + str(majNumber)) # TODO: delete

def runTests():
    test_findMajorityNumber()

