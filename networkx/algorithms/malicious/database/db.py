import networkx as nx

basic_RG = nx.DiGraph()
basic_RG.add_nodes_from(range(6, 10))
edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
basic_RG.add_edges_from(edges)

stupid_RG = nx.DiGraph()
stupid_RG.add_nodes_from(range(1, 7))
edges = [(1, 4), (2, 5), (3, 6)]
stupid_RG.add_edges_from(edges)

fork_DG = nx.DiGraph()
fork_DG.add_nodes_from(range(1, 4))
edges = [(1, 2), (2, 3)]
fork_DG.add_edges_from(edges)

fork_v1_DG = nx.DiGraph()
fork_v1_DG.add_nodes_from(range(1, 15))
edges = [(1, 4), (2, 6), (3, 5), (4, 7), (5, 8), (5, 10), (10, 10)]
fork_v1_DG.add_edges_from(edges)

stupid_DG_v1 = nx.DiGraph()
stupid_DG_v1.add_nodes_from(range(1, 7))
edges = [(1, 4), (2, 5), (3, 6)]
stupid_DG_v1.add_edges_from(edges)

basic_DG_v1 = nx.DiGraph()
basic_DG_v1.add_nodes_from(range(1, 12))
edges = [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 7),
         (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
basic_DG_v1.add_edges_from(edges)


basic_DG_v2 = nx.DiGraph()
basic_DG_v2.add_nodes_from(range(1, 12))
edges = [(1, 3), (2, 6), (4, 5), (3, 8), (6, 7), (6, 8),
         (6, 9), (5, 7), (9, 7), (9, 8), (9, 9), (8, 8)]
basic_DG_v2.add_edges_from(edges)

basic_DG_v3 = nx.DiGraph()
basic_DG_v3.add_nodes_from(range(1, 12))
edges = [(1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 7),
         (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
basic_DG_v3.add_edges_from(edges)

basic_DG_v4 = nx.DiGraph()
basic_DG_v4.add_nodes_from(range(1, 12))
edges = [(1, 5), (2, 6), (3, 4), (4, 5), (5, 8), (6, 7),
         (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
basic_DG_v4.add_edges_from(edges)

basic_DG_v5 = nx.DiGraph()
basic_DG_v5.add_nodes_from(range(1, 14))
edges = [(1, 11), (2, 12), (3, 10), (11, 6), (12, 6), (12, 7),
         (12, 5), (10, 5), (6, 6), (7, 6), (7, 7), (7, 5)]
basic_DG_v5.add_edges_from(edges)

suspected_viruses = {
    'basic_v1': basic_DG_v1, 'basic_v2': basic_DG_v2, 'basic_v3': basic_DG_v3,
    'basic_v4': basic_DG_v4, 'basic_v5': basic_DG_v5, 'stupid_v1': stupid_DG_v1,
    'fork_v1': fork_v1_DG
}

virus_data = {'basic_code': basic_RG,
              'stupid_code': stupid_RG, 'fork_code': fork_DG}
