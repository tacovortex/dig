import logic_gates as gates
import graph as gr
import clock as clk

if __name__ == "__main__":
    and_top = gates.And()
    and_bottom = gates.And()
    nor_top = gates.Nor()
    nor_bottom = gates.Nor()
    not_gate = gates.Not()
    clock = clk.Clock(period=4)
    data = gates.StimulusVector([1, 0, 1, 1, 0, 1, 1, 0])

    graph = gr.Graph()
    graph.add_edge(gr.Edge(data, and_bottom))
    graph.add_edge(gr.Edge(data, not_gate))
    graph.add_edge(gr.Edge(not_gate, and_top))
    graph.add_edge(gr.Edge(clock, and_top))
    graph.add_edge(gr.Edge(clock, and_bottom))

    graph.add_edge(gr.Edge(and_top, nor_top))
    graph.add_edge(gr.Edge(and_bottom, nor_bottom))
    graph.add_edge(gr.Edge(nor_top, nor_bottom))
    graph.add_edge(gr.Edge(nor_bottom, nor_top))

    sim_len = len(data.instream)
    print(data.instream)
    out_str = ""
    out_clk = ""
    for t in range(0, sim_len):
        graph.update()
        out_str += f"{nor_top.val} "
        out_clk += f"{clock.val} "

    print(f"clock: {out_clk}")
    print(f"output:  {out_str}")
    print("done")


