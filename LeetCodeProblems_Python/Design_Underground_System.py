class UndergroundSystem:

    def __init__(self):
        self.dict = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        if id not in self.dict.keys():
            self.dict[id] = []
        self.dict[id].append([stationName, t])

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.dict[id].append([stationName, t])

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # if even in then check in if odd the checkout
        total_time = 0
        count = 0
        for v in self.dict.values():
            for i in range(0, len(v)-1, 2):
                if v[i][0] == startStation and v[i+1][0] == endStation:
                    total_time += v[i+1][1] - v[i][1]
                    count += 1
        return total_time / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)