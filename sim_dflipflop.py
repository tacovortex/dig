import logic_gates as gates
import clock as clk
import graph as gr

if __name__ == "__main__":
    data = gates.StimulusVector([1, 0, 1, 1, 0, 1, 1, 0])
    nand_b1 = gates.Nand()
    nand_b2 = gates.Nand()
    nand_b3 = gates.Nand()
    nand_b4 = gates.Nand()
    nand_f1 = gates.Nand()
    nand_f2 = gates.Nand()

    clock = clk.Clock(period=4)

    graph = gr.Graph()
    graph.add_edge()
