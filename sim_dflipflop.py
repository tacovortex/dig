import logic_gates as gates
import graph as gr
import simulator as sim

if __name__ == "__main__":
    data = gates.StimulusVector([1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0], "data")
    nand_b1 = gates.Nand("nand_b1")
    nand_b2 = gates.Nand("nand_b2")
    nand3_b3 = gates.Nand3("nand3_b3")
    nand_b4 = gates.Nand("nand_b4")
    nand_f1 = gates.Nand("nand_f1")
    nand_f2 = gates.Nand("nand_f2")

    clock_data = gates.StimulusVector([0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], "clock")

    graph = gr.Graph()

    graph.add_edge(gr.Edge(nand3_b3, nand_b4))

    graph.add_edge(gr.Edge(nand_b4, nand3_b3))
    graph.add_edge(gr.Edge(clock_data, nand3_b3))
    graph.add_edge(gr.Edge(nand_b2, nand3_b3))

    graph.add_edge(gr.Edge(clock_data, nand_b2))
    graph.add_edge(gr.Edge(nand_b1, nand_b2))

    graph.add_edge(gr.Edge(data, nand_b4))

    graph.add_edge(gr.Edge(nand_b2, nand_b1))
    graph.add_edge(gr.Edge(nand_b4, nand_b1))

    graph.add_edge(gr.Edge(nand3_b3, nand_f2))
    graph.add_edge(gr.Edge(nand_f1, nand_f2))

    graph.add_edge(gr.Edge(nand_b2, nand_f1))
    graph.add_edge(gr.Edge(nand_f2, nand_f1))

    out_str = ""
    out_neg = ""
    out_clk = ""
    out_data = ""

    sim_ff = sim.Simulator(graph, [clock_data, data, nand_f1, nand_f2])
    sim_ff.simulate()

    # for i in range(0, len(data.instream)):
    #     graph.update()
    #     out_str += "1 " if nand_f1.val else "0 "
    #     out_neg += "1 " if nand_f2.val else "0 "
    #     out_clk += "1 " if clock_data.val == 1 else "0 "
    #     out_data += "1 " if data.val == 1 else "0 "
    #
    # print(f"data: : {out_data}")
    # print(f"clk   : {out_clk}")
    # print(f"qout  : {out_str}")
    # print(f"nout  : {out_neg}")

