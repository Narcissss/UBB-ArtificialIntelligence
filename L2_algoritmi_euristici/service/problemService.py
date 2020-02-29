from typing import List, Tuple, Dict
from domain.problem import ProblemResult, Problem


class ProblemService:

    def __init__(self):
        pass

    """
    Complexity: O(n*n) - time, O(n) - additional space
        n - number of cities
    """
    def findShothestPath_Greedy(self, problem: Problem) -> ProblemResult:
        totalTime = 0
        startCity = 0
        clientCity = problem.numberOfCities - 1
        cities = []
        cities.append(startCity)

        totalTime += self._calculateShortestPath(startCity, clientCity, problem.distances, cities, problem.numberOfCities)
        totalTime += self._calculateShortestPath(clientCity, startCity, problem.distances, cities, problem.numberOfCities)
        
        return ProblemResult(problem.numberOfCities, cities, totalTime)

    def _calculateShortestPath(self, startCity: int, endCity: int, distances: List[List[int]], cities: List[int], cityCount: int) -> int:
        visited = [False] * cityCount
        totalTime = 0
        currentCity = startCity
        visited[startCity] = True
        
        while currentCity != endCity:
            shorthestDistanceToNextCity = self._findShorthestDistanceToNextCity(distances[currentCity], visited)
            currentCity = shorthestDistanceToNextCity["city"]
            totalTime += shorthestDistanceToNextCity["distance"]
            cities.append(currentCity)
            visited[currentCity] = True
        return totalTime

    """
    Evaluation function - f
    """
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


