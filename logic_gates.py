import uuid


class Nor:
    def __init__(self, label=""):
        self.val = False
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, in_nodes):
        self.val = not (in_nodes[0].val or in_nodes[1].val)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class And:
    def __init__(self, label=""):
        self.val = False
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, in_nodes):
        self.val = in_nodes[0].val and in_nodes[1].val

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Nand3:
    def __init__(self, label=""):
        self.val = False
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, in_nodes):
        self.val = not (in_nodes[0].val and in_nodes[1].val and in_nodes[2].val)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Nand:
    def __init__(self, label=""):
        self.val = False
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, in_nodes):
        self.val = not (in_nodes[0].val and in_nodes[1].val)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Not:
    def __init__(self, label=""):
        self.val = False
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, in_nodes):
        self.val = not in_nodes[0].val

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class Stimulus:
    def __init__(self, val, label=""):
        self.val = val
        self.id = uuid.uuid4()
        self.label = label

    def compute(self, whatever):
        pass

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id == other.id


class StimulusVector:
    def __init__(self, instream, label=""):
        self.instream = instream
        self.index = 0
        self.id = uuid.uuid4()
        self.val = False
        self.label = label

    def compute(self, ignore):
        self.val = self.instream[self.index]
        self.index = self.index + 1

