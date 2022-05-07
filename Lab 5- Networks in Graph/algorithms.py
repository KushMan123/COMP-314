import networkx as nx

def numberOfNodes(graph):
    return len(nx.nodes(graph))

def numberOfEdges(graph):
    return len(nx.edges(graph))

def graphDesity(vertexs,edges):
    density=0
    if vertexs > 1:
        density= (2*edges/(vertexs*(vertexs-1)))
    return density

def graphDiameter(G):
    distance=0
    nodes=list(G.nodes())
    visited=[]
    try:
        for i in range(0,len(nodes)):
            visited.append(i)
            for j in range(1,len(nodes)):
                if j not in visited:
                    shortest_distance=nx.shortest_path_length(G,source=nodes[i],target=nodes[j])
                    if shortest_distance>=distance:
                        distance=shortest_distance
    except:
        return ("Inifite Path Length found because graph is not connected")
    return distance

def clusterCoefficient(G):
    C={}
    for i in G.nodes():
        e=0
        k=len(G.adj[i])
        for u in G.adj[i]:
            for v in G.adj[i]:
                if u==v:
                    continue
                if G.has_edge(u,v):
                    e+=1
        if k<2:
            C[i]=0
        else:
            e=e/2
            C[i]=(2*e)/(k*(k-1))
    total_C=0
    for i in G.nodes():
        total_C=total_C+C[i]
    return total_C/len(G.nodes())

def nodeDegree(G,v):
    return len(G.adj[v])

def degreeDistribution(G):
    d=[]
    x=[]
    y=[]
    nodes=len(G.nodes())
    for i in G.nodes():
        degree=nodeDegree(G,i)
        d.append(degree)
    for i in range(0,max(d)+1):
        x.append(i)
        y.append((d.count(i)/nodes))
    return x,y