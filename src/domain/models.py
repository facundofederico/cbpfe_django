from pandas import DataFrame

# Create your models here.
class ClusterStatistics():

    def __init__(self, cluster_elements: DataFrame) -> None:
        population = len(cluster_elements)
        profit_mean: cluster_elements.profit.mean()
        cost_mean: cluster_elements.cost.mean()
        profit_sd: cluster_elements.profit.std()
        cost_sd: cluster_elements.cost.std()
