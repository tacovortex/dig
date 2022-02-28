HIGH = True
LOW = False


class Term:
    def __init__(self, val=None):
        self.val = val

# maybe don't need this
# class Connection:
#     def __init__(self, term_a, term_b):
#         self.val = LOW
#         self.term_a = term_a
#         term_a.val = self.val
#         self.term_b = term_b
#         term_b.val = self.val


class And:
    def __init__(self):
        self.a: Term = Term()
        self.b: Term = Term()
        self.out_val = Term()
        self.out_nodes = []

    def set_a(self, term_a):
        self.a = term_a
        self.update()

    def set_b(self, term_b):
        self.b = term_b
        self.update()

    def add_out_node(self, out_node):
        self.out_nodes.append(out_node)

    def update(self):
        if self.a is None or self.b is None or self.a.val is None or self.b.val is None:
            self.out_val.val = None
            self.update_out_nodes()
        else:
            self.out_val.val = self.a.val and self.b.val
            self.update_out_nodes()

    def update_out_nodes(self):
        for node in self.out_nodes:
            node.update()
        
        
class Or:
    def __init__(self, term_a=None, term_b=None, out_node=None):
        self.a: Term = term_a if term_a is not None else Term()
        self.b: Term = term_b if term_b is not None else Term()
        self.out_val = Term
        self.update()
        self.out_node = out_node

    def set_a(self, term_a):
        self.a = term_a
        self.update()
        self.update_out_node()

    def set_b(self, term_b):
        self.b = term_b
        self.update()
        self.update_out_node()

    def set_out_node(self, out_node):
        self.out_node = out_node

    def update(self):
        if self.a.val is None or self.b.val is None:
            self.out_val.val = None
        else:
            self.out_val.val = self.a.val or self.b.val

    def update_out_node(self):
        self.out_node.update()


class Nor:
    def __init__(self):
        self.a: Term = Term()
        self.b: Term = Term()
        self.out_val = Term()
        self.out_nodes = []

    def set_a(self, term):
        self.a = term
        self.update()

    def set_b(self, term):
        self.b = term
        self.update()

    def add_out_node(self, out_node):
        self.out_nodes.append(out_node)

    def update(self):
        if self.a is None or self.b is None or self.a.val is None or self.b.val is None:
            self.out_val.val = None
            self.update_out_nodes()
        else:
            self.out_val.val = not (self.a.val or self.b.val)
            self.update_out_nodes()

    def update_out_nodes(self):
        for node in self.out_nodes:
            node.update()


class Not:
    def __init__(self):
        self.input: Term = Term()
        self.out_val = Term()
        self.out_nodes = []

    def set_a(self, term):
        self.input = term
        self.update()

    def add_out_node(self, out_node):
        self.out_nodes.append(out_node)

    def update(self):
        if self.input is None:
            self.out_val.val = None
        elif self.input.val is None:
            self.out_val.val = None
            self.update_out_nodes()
        else:
            self.out_val.val = not self.input.val
            self.update_out_nodes()

    def update_out_nodes(self):
        for node in self.out_nodes:
            node.update()
    