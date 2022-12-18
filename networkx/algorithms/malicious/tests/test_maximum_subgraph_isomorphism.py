"""
    Tests for maximum_subgraph_isomorphism.
"""

import pytest
import networkx as nx
from networkx.algorithms.malicious.maximum_subgraph_isomorphism import find_max__edges_of_sub_isomorphism_graph


class TestMaxumumSubgraphIsomorphism:
    # basic_code reduced garph
    basic_RG = nx.DiGraph()
    basic_RG.add_nodes_from(range(6, 10))
    edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
    basic_RG.add_edges_from(edges)

    # basic_code_v1 reduced garph
    # Variable renaming
    basic_RG_v1 = nx.DiGraph()
    basic_RG_v1.add_nodes_from(range(6, 10))
    edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
    basic_RG_v1.add_edges_from(edges)

    # basic_code_v2 reduced garph
    # Statement reordering
    basic_RG_v2 = nx.DiGraph()
    basic_RG_v2.add_nodes_from(range(6, 10))
    edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
    basic_RG_v2.add_edges_from(edges)

    # basic_code_v3 reduced garph
    # Format alternation
    basic_RG_v3 = nx.DiGraph()
    basic_RG_v3.add_nodes_from(range(6, 10))
    edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
    basic_RG_v3.add_edges_from(edges)

    # basic_code_v4 reduced garph
    # Statement replacement
    basic_RG_v4 = nx.DiGraph()
    basic_RG_v4.add_nodes_from(range(6, 10))
    edges = [(6, 7), (6, 8), (6, 9), (8, 8), (9, 7), (9, 8), (9, 9)]
    basic_RG_v4.add_edges_from(edges)

    # basic_code_v5 reduced garph
    # Spaghetti code
    basic_RG_v5 = nx.DiGraph()
    basic_RG_v5.add_nodes_from((5, 6, 7, 12))
    edges = [(6, 6), (7, 5), (7, 6), (7, 7), (12, 7), (12, 5), (12, 6)]
    basic_RG_v5.add_edges_from(edges)
    ###############################################

    # stupid code reduced garph
    stupid_RG = nx.DiGraph()
    stupid_RG.add_nodes_from(range(1, 7))
    edges = [(1, 4), (2, 5), (3, 6)]
    stupid_RG.add_edges_from(edges)

    # stupid_code_v1 reduced garph
    # variable renaming
    stupid_RG_v1 = nx.DiGraph()
    stupid_RG_v1.add_nodes_from(range(1, 7))
    edges = [(1, 4), (2, 5), (3, 6)]
    stupid_RG_v1.add_edges_from(edges)
    ###############################################

    # fork_code reduced garph
    # fork code
    fork_RG = nx.DiGraph()
    fork_RG.add_nodes_from(range(1, 7))
    edges = [(1, 2), (2, 3)]
    fork_RG.add_edges_from(edges)

    # fork_code_v1 reduced garph
    # junk code insertion
    fork_R1_RG = nx.DiGraph()
    fork_R1_RG.add_nodes_from(range(1, 15))
    edges = [(1, 4), (2, 6), (3, 5), (4, 7), (5, 8), (5, 10), (10, 10)]
    fork_R1_RG.add_edges_from(edges)

    def test_basic_code_vs_basic_code_v1(self):
        """
        Checks the basic original code from the paper:
        http://rosaec.snu.ac.kr/publish/2010/T2/KiMo-GECCO-2010.pdf
        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.basic_RG, self.basic_RG_v1) == len(self.basic_RG.edges)

    def test_basic_code_vs_basic_code_v2(self):
        """
        Checks the first varient (Variable renaming) of the basic original code from the paper:
        http://rosaec.snu.ac.kr/publish/2010/T2/KiMo-GECCO-2010.pdf
        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.basic_RG, self.basic_RG_v2) == len(self.basic_RG.edges)

    def test_basic_code_vs_basic_code_v3(self):
        """
        Checks the second varient (Statement reordering) of the basic original code from the paper:
        http://rosaec.snu.ac.kr/publish/2010/T2/KiMo-GECCO-2010.pdf
        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.basic_RG, self.basic_RG_v3) == len(self.basic_RG.edges)

    def test_basic_code_vs_basic_code_v4(self):
        """
        Checks the third varient (Format alternation) of the basic original code from the paper:
        http://rosaec.snu.ac.kr/publish/2010/T2/KiMo-GECCO-2010.pdf

        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.basic_RG, self.basic_RG_v4) == len(self.basic_RG.edges)

    def test_basic_code_vs_basic_code_v5(self):
        """
        Checks the fourth varient (Statement replacement) of the basic original code from the paper:
        http://rosaec.snu.ac.kr/publish/2010/T2/KiMo-GECCO-2010.pdf

        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.basic_RG, self.basic_RG_v5) == len(self.basic_RG.edges)

    def test_stupid_code_vs_stupid_code_v1(self):
        """
        Checks the stupid_code example that we made up:
        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.stupid_RG, self.stupid_RG_v1) == len(self.stupid_RG.edges)

    def test_fork_code_vs_fork_code_v1(self):
        """
        Checks the first variant of stupid_code:
        """
        assert find_max__edges_of_sub_isomorphism_graph(
            self.fork_RG, self.fork_R1_RG) == len(self.fork_RG.edges)
