import pandas as pd
import networkx as nx
from algorithms import numberOfNodes,numberOfEdges,graphDesity,graphDiameter,clusterCoefficient, degreeDistribution
import matplotlib.pyplot as plt

def importGraph1():
    header_list=['a','b','w']
    E=pd.read_csv("graph_data/eco-stmarks.edges", sep=" ", header=None, names=header_list)
    G= nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def importGraph2():
    header_list=["a","b","w"]
    E=pd.read_csv("graph_data/soc-advogato.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def importGraph3():
    header_list=["a","b","w"]
    E=pd.read_csv("graph_data/bio-DM-HT.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def importGraph4():
    header_list=["a","b","w"]
    E=pd.read_csv("graph_data/bio-CE-HT.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def importGraph5():
    header_list=["a","b","w"]
    E=pd.read_csv("graph_data/bio-CE-GN.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def importGraph6():
    header_list=["a","b","w"]
    E=pd.read_csv("graph_data/bio-CE-PG.edges", sep=" ", header=None, names=header_list)
    G=nx.from_pandas_edgelist(E,"a","b",["w"])
    return G

def graphDetails(graph, graphName):
    print(f'--------------{graphName}-------------')
    print("Number of Nodes",numberOfNodes(graph))
    print("Number of Edges",numberOfEdges(graph))
    print("Graph Density",graphDesity(numberOfNodes(graph),numberOfEdges(graph)))
    print("Graph Diameter",graphDiameter(graph))
    print("Average Cluster Coefficient",clusterCoefficient(graph))

def degreeDistributionPlot(graph):
    x,y=degreeDistribution(graph)
    plt.plot(x,y)
    plt.xlabel("Degree")
    plt.ylabel("P(k)")
    plt.show()

if __name__=="__main__":
    graph1=importGraph1()
    graph2=importGraph2()
    graph3=importGraph3()
    graph4=importGraph4()
    graph5=importGraph5()
    graph6=importGraph6()
    # graphDetails(graph1, "eco-stmarks")
    # graphDetails(graph2, "soc-advogato")
    # graphDetails(graph3, "bio-DM-HT")
    # graphDetails(graph4, "bio-grid-worms")
    # graphDetails(graph5, "bio-CE-GN")
    # graphDetails(graph6, "bio-CE-PG")
    degreeDistributionPlot(graph6)