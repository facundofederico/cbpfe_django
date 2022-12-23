from numpy import ndarray
import math
from scipy.spatial.distance import squareform, pdist
from pandas import DataFrame

def hamming_distance(str1: str, str2: str) -> float:
    """
    Hamming distance between two strings with the same length.
    :param list1: First string.
    :param list2: Second string.
    :return: proportional Hamming distance, with values ranging between 0 and 1.
    """
    if len(str1) != len(str2):
        raise Exception("The provided strings must have the same length.")

    distance = 0
    
    length = len(str1)
    for index in range(length):
        if str1[index] != str2[index]:
            distance += 1
            
    return distance/length

def get_distance_matrix(data: DataFrame) -> ndarray[float]:
    """
    Distance matrix between solutions
    :param data: list of solutions
    :return: redundant distance matrix
    """

    max_profit = max(solution[0] for solution in data)
    max_cost = max(solution[1] for solution in data)

    def solution_distance(solution1: list, solution2: list) -> float:
        """
        Distance between two solutions
        :param sol1: first solution
        :param sol2: second solution
        :return: distance, expresed as a value between 0 and 1.
        """

        cost_dist = abs((float(solution1[1]) - float(solution2[1])) / max_cost)
        prof_dist = abs(float(solution1[0]) - float(solution2[0])) / max_profit
        req_dist = hamming_distance(solution1[2], solution2[2])
        stk_dist = hamming_distance(solution1[3], solution2[3])

        # The final value is always between 0 and 1.
        distance = math.sqrt(cost_dist**2 + prof_dist**2 + req_dist**2 + stk_dist**2)

        return distance

    # Calculate the distance between each pair of quasi-optimal solutions.
    distance_matrix = squareform(pdist(data, solution_distance))
    
    return distance_matrix