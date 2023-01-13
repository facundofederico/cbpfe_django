from django.shortcuts import render
from file_loader.loader import get_pareto_front, get_requirements, get_stakeholders
from domain.algorithms import get_dataframe, get_linkage_matrix
from domain.filters import get_filter
from .plots import get_dendogram, get_scatterplot

# Create your views here.
def dashboard_view(request, *args, **kwargs):
    data = get_dataframe(get_pareto_front())
    reqs_catalog = get_requirements()
    stks_catalog = get_stakeholders()

    current_level = 0
    cluster_chosen_per_level = []
    filter = get_filter(
                current_level= current_level,
                cluster_chosen_per_level= cluster_chosen_per_level,
                data= data)

    linkage_matrix = get_linkage_matrix(
                        data= data,
                        filter= filter,
                        desired_cluster_number= 3,
                        current_level= current_level)

    scatterplot= get_scatterplot(
                    data= data,
                    cluster_column= "Level {}".format(current_level))

    dendogram= get_dendogram(linkage_matrix= linkage_matrix)

    context = {}

    return render(request, 'dashboard/dashboard.html', context)