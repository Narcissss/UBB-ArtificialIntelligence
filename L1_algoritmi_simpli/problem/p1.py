
"""
Să se determine ultimul (din punct de vedere alfabetic) cuvânt care poate apărea într-un text
care conține mai multe cuvinte separate prin ” ” (spațiu).
De ex. ultimul (dpdv alfabetic) cuvânt din ”Ana are mere rosii si galbene” este
cuvântul "si".

Complexitate: O(n) - timp, O(1) - spatiu suplimentar
    n - lungimea textului
"""

from problem.utils import getAbsolutePath


def readWords(path: str) -> list:
    fileD = open(path, 'r')
    words = []
    for line in fileD:
        for word in line.split():
            words.append(word)
    return words

def getLastword(words: list) -> str:
    if not words:
        return "---"
    lastWord = words[0]
    for word in words:
        if word > lastWord:
            lastWord = word
    return lastWord

def test_getLastWord() -> None:
    path = getAbsolutePath(__file__, "../data/p1.txt")
    words = readWords(path)
    lastWord = getLastword(words)
    assert(lastWord == "si")
    print("P1: " + lastWord) # TODO: delete

def runTests() -> None:
    test_getLastWord()
