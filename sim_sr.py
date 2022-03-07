import graph as gr
import logic_gates as gates

if __name__ == "__main__":
    nor1 = gates.Nor()
    nor2 = gates.Nor()

    s = gates.Stimulus(True)
    r = gates.Stimulus(False)

    graph = gr.Graph()

    graph.add_edge(gr.Edge(s, nor1))
    graph.add_edge(gr.Edge(nor2, nor1))
    graph.add_edge(gr.Edge(nor1, nor2))
    graph.add_edge(gr.Edge(r, nor2))

    graph.update()

    print("s = f, r = t")

    s.val = False
    r.val = False

    graph.update()
    print("s = f, r = f")

    s.val = False
    r.val = True

    graph.update()
    print("s = f, r = t")

    # invalid
    s.val = True
    r.val = True

    graph.update()
    print("s = t, r = t")



