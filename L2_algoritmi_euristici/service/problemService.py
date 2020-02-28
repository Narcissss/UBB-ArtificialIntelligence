from typing import List, Tuple, Dict
from domain.problem import ProblemResult, Problem


class ProblemService:

    def __init__(self):
        self._startCity = 0

    """
    Complexity: O(n*n) - time, O(n) - additional space
        n - number of cities
    """
    def findShothestPath_Greedy(self, problem: Problem) -> ProblemResult:
        visited = [False] * problem.numberOfCities
        totalTime = 0
        currentCity = self._startCity
        visited[currentCity] = True
        visitedCities = 1
        cities = [currentCity] # start city
        
        while visitedCities < problem.numberOfCities:
            shorthestDistanceToNextCity = self._findShorthestDistanceToNextCity(problem.distances[currentCity], visited)
            currentCity = shorthestDistanceToNextCity["city"]
            totalTime += shorthestDistanceToNextCity["distance"]
            cities.append(currentCity)
            visited[currentCity] = True
            visitedCities += 1
        totalTime += problem.distances[currentCity][0]

        return ProblemResult(problem.numberOfCities, cities, totalTime)

    def _findShorthestDistanceToNextCity(self, distances: List[int], visited: List[bool]) -> Dict[str, int]:
        minDistance = 999 * 999
        city = 0
        nextCity = -1
        for distance in distances:
            if distance < minDistance and not visited[city]:
                minDistance = distance
                nextCity = city
            city += 1
        
        return { "city" : nextCity, "distance" : minDistance}


def test_findShorthestDistanceToNextCity():
    dist = [0, 10, 5, 30, 10]
    visited = [True, True, True, False, False]
    res = ProblemService()._findShorthestDistanceToNextCity(dist, visited)
    assert(res["city"] == 4 and res["distance"] == 10)

test_findShorthestDistanceToNextCity()


