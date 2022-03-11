class Simulator:
    def __init__(self, graph, watch):
        self.graph = graph
        self.sim_len = len(graph.stimuli[0].instream)
        for stim in graph.stimuli:
            if len(stim.instream) != self.sim_len:
                # TODO throw some errors or something
                pass
        self.watch_list = {}
        for node in watch:
            self.watch_list[node] = []

    def simulate(self):
        for i in range(0, self.sim_len):
            self.graph.update()
            for node_entry in self.watch_list.items():
                node_entry[1].append("1" if node_entry[0].val else "0")

        for node_entry in self.watch_list.items():
            print(f"{node_entry[0].label}")
            print(f"{node_entry[1]}")

