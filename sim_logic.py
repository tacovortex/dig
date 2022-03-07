import graph as gr
import logic_gates


def dfs(root, graph_data):
    visited = set()

    def dfs_walk(node):
        visited.add(node)
        node.compute(graph_data.node_index[node].from_nodes)
        for to_node in graph_data.node_index[node].to_nodes:
            if to_node not in visited:
                dfs_walk(to_node)

    dfs_walk(root)


if __name__ == "__main__":
    andgate = logic_gates.And()
    notgate = logic_gates.Not()
    in_a = logic_gates.Stimulus(True)
    in_b = logic_gates.Stimulus(True)

    graph = gr.Graph()
    graph.add_edge(gr.Edge(in_a, andgate))
    graph.add_edge(gr.Edge(in_b, andgate))
    graph.add_edge(gr.Edge(andgate, notgate))

    # for stim in graph.stimuli:
    #     dfs(stim, graph)
    graph.update()

    print("Done")




