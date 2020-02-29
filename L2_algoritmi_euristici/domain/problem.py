
from typing import List

class TSProblem:
    """
    Traveling Salesman Problem
    """

    def __init__(self, textFormat: str):
        self.numberOfCities = 0
        self.distances = []
        self._createTSProblem(textFormat)

    def _createTSProblem(self, textFormat):
        lines = textFormat.split('\n')
        self.numberOfCities = int(lines[0])
        for line in lines[1:]:
            if line:
                self.distances.append([int(number) for number in line.split(',')])


class TSProblemResult:

    def __init__(self, numberOfCities: int, cities: List[int], totalTime: int):
        self.numberOfCities = numberOfCities
        self.cities = cities
        self.time = totalTime
    
    def __str__(self) -> str:
        result = ""
        result += str(self.numberOfCities) + "\n"
        for city in self.cities[:-1]:
            result += str(city) + ","
        result += str(self.cities[-1]) + "\n"
        result += str(self.time)
        return result