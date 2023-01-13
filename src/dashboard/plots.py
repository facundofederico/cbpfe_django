from pandas import DataFrame
from plotly.figure_factory import create_dendrogram
from plotly.graph_objects import Figure
from plotly.express import scatter
from numpy import ndarray
# from wordcloud import WordCloud, STOPWORDS

# def get_wordcloud(data: DataFrame, category: str, category_catalog: dict) -> WordCloud:
#     """
#     Generates a wordcloud to represent a set of data in regard to a certain category.
#     :param data: data to represent as a wordcloud.
#     :param category: category to analyze ('reqs' for requirements, 'stks' for stakeholders).
#     :param category_catalog: catalog of requirements/stakeholders with their keywords.
#     :return: wordcloud that represents the main requirements/stakeholders in a set of data.
#     """
#     cluster_words = []

#     # for each row
#     for r in data["id"]:
#         # for each element in catalog
#         for i in range(len(category_catalog)):
#             # if the element is in that solution
#             if data[category][r][i] == '1':
#                 # add element words to cluster words
#                 cluster_words.extend(category_catalog[i]['keys'])

#     # get text from words
#     text = ' '.join(cluster_words)

#     wordcloud = WordCloud(
#                         width= 800,
#                         height= 400,
#                         background_color='white',
#                         stopwords= STOPWORDS,
#                         min_font_size= 8,
#                         collocations= False
#                         )
    
#     wordcloud.generate(text)

#     return wordcloud

def get_dendogram(linkage_matrix: ndarray) -> Figure:
    """
    Generates a wordcloud to represent a set of data in regard to a certain category.
    :param data: data to represent as a wordcloud.
    :param category: category to analyze ('reqs' for requirements, 'stks' for stakeholders).
    :param category_catalog: catalog of requirements/stakeholders with their keywords.
    :return: dendogram figure.
    """
    dendogram = create_dendrogram(linkage_matrix)

    dendogram.update_xaxes(showticklabels=False)
    dendogram.update_yaxes(showticklabels=False)
    dendogram.update_layout(margin=dict(l=0, r=0, b=0, t=0))

    return dendogram

def get_scatterplot(data: DataFrame, cluster_column: str) -> Figure:
    """
    Generates a scatterplot to represent a set of data.
    :param data: data to represent as a scatterplot.
    :param cluster_column: column to use for color marks.
    :return: scatterplot figure.
    """
    scatterplot = scatter(
                        data_frame= data,
                        x= "profit",
                        y= "cost",
                        color= cluster_column,
                        hover_data= ['id']
                        )

    scatterplot.update_layout(coloraxis_showscale=False, margin=dict(l=0, r=0, b=0, t=0))

    return scatterplot