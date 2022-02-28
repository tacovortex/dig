from gates import *

set_gate = Nor()
reset_gate = Nor()

set_gate.set_a(reset_gate.out_val)
reset_gate.set_a(set_gate.out_val)


stream_s = [LOW, LOW, HIGH, HIGH]
stream_r = [LOW, HIGH, LOW, HIGH]

if __name__ == "__main__":
    cycle_count = 0
    term_r = Term()
    term_s = Term()
    for i in range(0, len(stream_s)):
        term_r.val = stream_r[i]
        term_s.val = stream_s[i]
        set_gate.set_b(term_s)
        reset_gate.set_b(term_r)