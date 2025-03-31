import pytest
import networkx as nx
from search import graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    
    G = graph.Graph('./data/tiny_network.adjlist')
    
    assert list(nx.bfs_tree(G.graph, source='31806696')) == G.bfs(source='31806696')

    
def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    G = graph.Graph('./data/citation_network.adjlist')
    
    assert list(nx.bfs_tree(G.graph, source='34916529')) == G.bfs(source='34916529')
    assert list(nx.shortest_path(G.graph, source='32025019', target='Hani Goodarzi')) == G.bfs(source='32025019', end='Hani Goodarzi')

    assert G.bfs(source='34916529',end='34858697') == None
    assert G.bfs(source='yolo',end='swag') == None

