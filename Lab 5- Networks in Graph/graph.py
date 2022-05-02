import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

header_list=['a','b','w']
E=pd.read_csv("graph_data/eco-stmarks.edges", sep=" ", header=None, names=header_list)
print(E.head())

G= nx.from_pandas_edgelist(E,"a","b",["w"])
nx.draw(G)
plt.show()
print(G)
print(nx.number_of_nodes(G))