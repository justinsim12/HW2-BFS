import networkx as nx
from collections import deque

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, source, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

                    #used github copolit and stack overflow

        """
        # Check if source is in the graph.
        if source not in self.graph.nodes:
            return None
        # If an end node is provided, check its existence.
        if end and end not in self.graph.nodes:
            return None  # or raise an exception if preferred

        Q = deque([source])
        visited_order = [source]    # To preserve the order of visitation.
        visited_set = {source}      # For fast membership checking.
        previous = {source: None}

        found = False
        while Q:
            v = Q.popleft()

            # If we have reached the target, break.
            if v == end:
                found = True
                break

            # Process neighbors
            for w in self.graph.neighbors(v):
                if w not in visited_set:
                    visited_order.append(w)
                    visited_set.add(w)
                    Q.append(w)
                    previous[w] = v

        # If no end was specified, return the full BFS order.
        if end is None:
            return visited_order

        # If the end node was not reached, return None.
        if not found:
            return None

        # Reconstruct the path from source to end.
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        path.reverse()
        return path