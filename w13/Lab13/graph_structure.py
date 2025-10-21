import matplotlib.pyplot as plt
import networkx as nx
from collections import deque


class graph_structure:
    def __init__(self):
        self.graph : dict[str , list[str]] = {}
    

    def add_edge(self , node : str , neighbor : str) -> None:
        if node not in self.graph: self.graph[node] = []
        if neighbor not in self.graph: self.graph[neighbor] = []

        self.graph[node].append(neighbor)
        self.graph[neighbor].append(node)
    

    def show_graph(self) -> None:
        for node , neighbors in self.graph.items(): print("{} -> {}".format(node , neighbors))
    

    def plot_graph(self , highlight_nodes = None , title = "graph") -> None:
        G = nx.Graph(self.graph)
        pos = nx.spring_layout(G , seed=42)
        plt.figure(figsize=[6 , 4])

        node_color = []
        for n in G.nodes():
            if highlight_nodes and n in highlight_nodes: node_color.append("lightcoral")
            else: node_color.append("skyblue")
        plt.title(title)
        nx.draw(
            G=G,pos=pos,
            with_labels=True,
            node_color=node_color,
            node_size=1200,
            font_size=12,
            font_weight="bold",
            edge_color="gray"
        )
        plt.show(block=False)
        plt.pause(2)
        plt.close()

    

    def bfs(self , start : str) -> None:
        if start not in self.graph.keys(): raise KeyError("{} is not in graph".format(start))
        visit : dict[str , bool] = {}
        q = deque()

        for node in self.graph.keys(): visit.update({node : False})

        q.append(start)
        visit[start] = True
        self.plot_graph(start , "BFS")
        while q:
            current = q.popleft()
            for v in self.graph[current]:
                if not visit[v]:
                    visit[v] = True
                    q.append(v)
                    self.plot_graph(v , "BFS")



    def dfs(self , start : str , visit=None) -> None:
        if start not in self.graph.keys(): raise KeyError("{} is not in graph".format(start))
        visit : set[str] = set() if visit == None else visit
        visit.add(start)
        self.plot_graph(start , "DFS")

        for v in self.graph[start]:
            if v not in visit: self.dfs(v , visit)


    




g = graph_structure()
g.add_edge("a" , "b")
g.add_edge("a" , "c")
g.add_edge("b" , "d")
g.add_edge("c" , "d")
g.add_edge("d" , "e")

g.show_graph()
#g.plot_graph()

g.bfs("a")
g.dfs("a")