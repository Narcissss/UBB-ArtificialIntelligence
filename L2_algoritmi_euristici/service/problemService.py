from typing import List, Tuple, Dict
from domain.problem import TSProblemResult, TSProblem


class ProblemService:

    def __init__(self):
        pass

    
    def findShothestPath_Greedy(self, problem: TSProblem) -> TSProblemResult:
        """
        Complexity: O(n*n) - time, O(n) - additional space
            n - number of cities
        """
        startCity = 0
        cities = [startCity]

        totalTime = self._calculateShortestPath(startCity, problem.distances, cities, problem.numberOfCities)

        return TSProblemResult(problem.numberOfCities, cities, totalTime)

    def _calculateShortestPath(self, startCity: int, distances: List[List[int]], cities: List[int], cityCount: int) -> int:
        visited = [False] * cityCount
        totalTime = 0
        currentCity = startCity
        visited[startCity] = True
        visitedCities = 1
        
        while visitedCities < cityCount:
            shorthestDistanceToNextCity = self._findShorthestDistanceToNextCity(distances[currentCity], visited)
            currentCity = shorthestDistanceToNextCity["city"]
            totalTime += shorthestDistanceToNextCity["distance"]
            cities.append(currentCity)
            visited[currentCity] = True
            visitedCities += 1
        totalTime += distances[currentCity][startCity]

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


