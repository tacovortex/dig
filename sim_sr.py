import graph as gr
import logic_gates as gates
import simulator as sim

if __name__ == "__main__":
    nor1 = gates.Nor("q0")
    nor2 = gates.Nor("q")

    s = gates.StimulusVector([0, 1, 0, 1], "sin")
    r = gates.StimulusVector([0, 0, 1, 1], "rin")

    graph = gr.Graph()

    graph.add_edge(gr.Edge(s, nor1))
    graph.add_edge(gr.Edge(nor2, nor1))
    graph.add_edge(gr.Edge(nor1, nor2))
    graph.add_edge(gr.Edge(r, nor2))

    sim_sr = sim.Simulator(graph, [s, r, nor1, nor2])
    sim_sr.simulate()

    # graph.update()

    # print("s = f, r = t")
    #
    # s.val = False
    # r.val = False
    #
    # graph.update()
    # print("s = f, r = f")
    #
    # s.val = False
    # r.val = True
    #
    # graph.update()
    # print("s = f, r = t")
    #
    # # invalid
    # s.val = True
    # r.val = True
    #
    # graph.update()
    # print("s = t, r = t")



