class Fancy:

    def __init__(self):
        self.sequence = []
        self.increment = 0
        self.multiply = 1
        self.MOD = 10**9 + 7

    def append(self, val: int) -> None:
        inverseMul = pow(self.multiply, self.MOD - 2, self.MOD)
        normalised = (val - self.increment) * inverseMul % self.MOD
        self.sequence.append(normalised) 

    def addAll(self, inc: int) -> None:
        self.increment = (self.increment + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.multiply = self.multiply * m % self.MOD
        self.increment = self.increment * m % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.sequence):
            return -1
        else:
            return (self.sequence[idx] * self.multiply + self.increment) % self.MOD


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)