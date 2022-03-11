from logic_gates import (
    Stimulus,
    StimulusVector
)


class Edge:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node


class NodeData:
    def __init__(self):
        self.to_nodes = []
        self.from_nodes = []


class Graph:
    def __init__(self):
        self.edge_list = []
        self.node_index = {}
        self.stimuli = []

    def add_edge(self, edge: Edge):
        self.edge_list.append(edge)
        if edge.to_node in self.node_index:
            self.node_index[edge.to_node].from_nodes.append(edge.from_node)
        else:
            node = NodeData()
            node.from_nodes.append(edge.from_node)
            self.node_index[edge.to_node] = node

        if edge.from_node in self.node_index:
            self.node_index[edge.from_node].to_nodes.append(edge.to_node)
        else:
            node = NodeData()
            node.to_nodes.append(edge.to_node)
            self.node_index[edge.from_node] = node

        if self.is_stimulus(edge.from_node) and edge.from_node not in self.stimuli:
            self.stimuli.append(edge.from_node)

    def update(self):
        for stim in self.stimuli:
            self.dfs(stim)
            stim.compute("")

    def dfs(self, root):
        visited = set()
        self.dfs_traverse(root, visited)

    def dfs_traverse(self, node, visited):
        visited.add(node)
        for to_node in self.node_index[node].to_nodes:
            to_node.compute(self.node_index[to_node].from_nodes)

        for to_node in self.node_index[node].to_nodes:
            if to_node not in visited:
                self.dfs_traverse(to_node, visited)

    def is_stimulus(self, in_put) -> bool:
        if isinstance(in_put, Stimulus):
            return True
        elif isinstance(in_put, StimulusVector):
            return True
        else:
            return False
