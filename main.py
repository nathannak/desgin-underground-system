from collections import Counter, defaultdict


class UndergroundSystem:
    def __init__(self):
        self.ids = {}
        self.pairs = defaultdict(int)
        self.freqs = Counter()

    def checkIn(self, id, stationName, t):
        self.ids[id] = (stationName, t)

    def checkOut(self, id, stationName, t):
        Name2, t2 = self.ids.pop(id)
        self.pairs[(Name2, stationName)] += (t - t2)
        self.freqs[(Name2, stationName)] += 1

    def getAverageTime(self, startStation, endStation):
        return self.pairs[startStation, endStation] / self.freqs[startStation, endStation]

if __name__ == '__main__':
    obj = UndergroundSystem()

    obj.checkIn(45, "Leyton", 3)
    obj.checkIn(32, "Paradise", 8)
    obj.checkIn(27, "Leyton", 10)

    obj.checkOut(45, "Waterloo", 15)
    obj.checkOut(27,"Waterloo",20)
    obj.checkOut(32,"Cambridge",22)

    print(obj.getAverageTime("Paradise", "Cambridge"))

