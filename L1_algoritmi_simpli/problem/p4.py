"""
 Să se determine cuvintele unui text care apar exact o singură dată în acel text.
De ex. cuvintele care apar o singură dată în ”ana are ana are mere rosii ana" sunt:
'mere' și 'rosii'

Complexitate: O(n) - timp, O(n) - spatiu sumplimentar
    n - lungimea textului
"""

from typing import List


def findUniqueWords(words: List[str]) -> List[int]:
    wordCounter = {}
    for word in words:
        if word in wordCounter: wordCounter[word] += 1
        else: wordCounter[word] = 1
    uniqueWords = []
    for word in wordCounter.keys():
        if wordCounter[word] == 1:
            uniqueWords.append(word)
    return uniqueWords

def test_findUniqueWords():
    words = "ana are ana are mere rosii ana".split()
    uniqueWords = findUniqueWords(words)
    expected = ["mere", "rosii"]
    assert(uniqueWords == expected)
    print("P4: " + str(uniqueWords)) # TODO: delete

def runTests():
    test_findUniqueWords()