class Clock:
    def __init__(self, period):
        self.val = True
        self.period = period
        self.phase = 0

    def compute(self, ignore):
        if self.phase == self.period / 2:
            self.val = not self.val
            self.phase = 0
        self.phase += 1
