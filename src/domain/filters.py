from numpy import logical_and
from pandas import DataFrame

def __get_filter_for_level(level: int, cluster_per_level: list[int], data: DataFrame) -> list[bool]:
    """
    Generates the boolean array used to filter the pareto-front by its level of clustering zoom
    :param level: level of clustering zoom.
    :param cluster_per_level: cluster choosen for each level.
    :param data: pareto-front as dataset.
    :return: boolean array
    """
    if level == 0:
        return [True] * len(data)

    column_title = "Level {}".format(level-1)
    cluster_number = cluster_per_level[level-1]

    filter = data[column_title] == cluster_number
    
    return filter

def get_filter(current_level: int, cluster_per_level: list[int], data: DataFrame) -> list[bool]:
    """
    Generates the boolean array used to filter the pareto-front for the clusters choosen for each level
    :param current_level: current level of clustering zoom.
    :param cluster_per_level: cluster choosen for each level.
    :param data: pareto-front as dataset.
    :return: boolean array
    """
    filter = [True] * len(data)

    for i in range(current_level):
        filter = logical_and(__get_filter_for_level(i+1, cluster_per_level, data), filter)
        if not(any(filter)):
            #An exception is raised if the resulting boolean array is all False
            raise Exception("There are no solutions that fulfill all restrictions")

    return filter