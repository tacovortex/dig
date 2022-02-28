from gates import *

stream_1 = [LOW, LOW, HIGH, HIGH]
stream_2 = [LOW, HIGH, LOW, HIGH]

and_gate = And()
not_gate = Not()

and_gate.add_out_node(not_gate)
not_gate.set_a(and_gate.out_val)

if __name__ == "__main__":
    cycle_counter = 0
    term_a = Term()
    term_b = Term()
    for i in range(0, len(stream_1)):
        cycle_counter += 1
        term_a.val = stream_1[i]
        term_b.val = stream_2[i]
        and_gate.set_a(term_a)
        and_gate.set_b(term_b)
        print(f"And: {and_gate.out_val.val}")
        print(f"Not: {not_gate.out_val.val}")


