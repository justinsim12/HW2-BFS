! [BuildStatus] (https://github.com/justinsim12/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)
Graph BFS Implementation

This repository contains a Graph class with a custom breadth-first search (BFS) method designed for graph traversal and shortest-path finding using an adjacency list. The BFS method can perform a full traversal or find the shortest path between two nodes, and it gracefully handles cases where nodes are missing or not connected.

Overview

The bfs method in the Graph class provides two primary functionalities:
	•	Full BFS Traversal:
When no target node is provided, the method returns a list of nodes in the order they are visited using BFS, starting from the source node.
	•	Shortest Path Finding:
When a target (end) node is specified, the method returns a list representing the shortest path from the source to the target. If no such path exists, the method returns None.

Additionally, the method checks for:
	•	Nonexistent Source: If the source node is not present in the graph, the method returns None.
	•	Nonexistent Target: If the target node is provided but does not exist in the graph, the method returns None (alternatively, you may choose to raise an exception based on your design).
	•	Disconnected Nodes: If there is no path between the source and target nodes, the method returns None.

How the Method Works
	1.	Input Validation:
The method first checks if the source node exists in the graph. If an end node is provided, it verifies its existence as well.
	2.	BFS Traversal:
Using a queue (deque), the method performs a standard BFS traversal from the source node.
	•	A visited_order list keeps track of the order of nodes as they are visited.
	•	A visited_set is used for fast membership checks.
	•	A previous dictionary is maintained to keep track of each node’s predecessor.
	3.	Path Reconstruction (if a target is provided):
When the target node is reached during the BFS, the method reconstructs the shortest path by backtracking through the previous dictionary from the target to the source. The path is then reversed to present the correct order from source to target.
	4.	Return Value:
	•	If no target node is provided, the method returns the full BFS traversal order.
	•	If a target is provided and reachable, the method returns the shortest path as a list.
	•	If a target is provided but unreachable, the method returns None.

Example Usage

from graph import Graph

# Initialize the graph using an adjacency list file.
G = Graph('./data/citation_network.adjlist')

# Perform a full BFS traversal starting from a given source node.
bfs_order = G.bfs(source='34916529')
print("BFS Order:", bfs_order)

# Find the shortest path from a source node to a target node.
shortest_path = G.bfs(source='32025019', end='Hani Goodarzi')
print("Shortest Path:", shortest_path)

# Check behavior when nodes are not connected.
result = G.bfs(source='34916529', end='34858697')
print("Path does not exist:", result)