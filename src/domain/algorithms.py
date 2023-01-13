from pandas import DataFrame
from .distances import get_distance_matrix
from scipy.cluster.hierarchy import linkage, fcluster
from numpy import ndarray
from .models import ClusterStatistics

def get_dataframe(pareto_front: dict) -> DataFrame:
    """
    Transforms the pareto front from a dict into a DataFrame.
    :param pareto_front: the pareto front in dict form.
    :return: the pareto front as a DataFrame.
    """
    data = DataFrame.from_dict(
                        data= pareto_front,
                        orient= 'index',
                        dtype= {
                            'id': int,
                            'profit': float,
                            'cost': float,
                            'reqs': str,
                            'stks': str
                        })

    return data

def get_linkage_matrix(data: DataFrame, filter: list[bool], desired_cluster_number: int, current_level: int) -> ndarray:
    """
    Returns hierarchical clustering on the dataframe. A column is added to the data that
    assigns a cluster for each value for the current level.
    :param data: dataset to cluster.
    :param filter: list of boolean that indicates which rows are going to be clustered.
    :param desired_cluster_number: max number of clusters to be generated.
    :param current_level: current level of clustering zoom.
    :return: linkage matrix, number of generated clusters.
    """
    # filter rows
    filtered_data = data.loc[filter]

    # get distance matrix for filtered data
    distance_matrix = get_distance_matrix(filtered_data)

    # get linkage matrix for hierarchical clustering
    linkage_matrix = linkage(distance_matrix, method="complete")

    # get a list with a cluster number for each value
    clusters = fcluster(linkage_matrix, desired_cluster_number, criterion='maxclust')

    # for each value in data, if value is in filter, add cluster number, else add None
    clusters = iter(clusters)
    clustering_column = [str(next(clusters)) if value else None for value in filter]

    # assign cluster column to the Level column. This creates the column if necessary
    data["Level {}".format(current_level)] = clustering_column

    return linkage_matrix

def get_cluster_statistics(filter: list[bool], current_level: int, data: DataFrame) -> list[ClusterStatistics]:
    """
    Get statistics of each cluster
    :param indices: list of boolean that indicates which rows are going to be clustered.
    :param nivel: level of clustering zoom.
    :n_generado_de_clusters: number of generated clusters (int)
    :return: dictionary of statistics
    """
    df = data.loc[filter]
    clustering_column = df["Level {}".format(current_level)]
    cluster_number = max(clustering_column)

    statistics = []
    for c in range(1, cluster_number+1):
        cluster_elements = df.loc[clustering_column == str(c)]

        stat = ClusterStatistics(cluster_elements)

        statistics[c] = stat
    return statistics