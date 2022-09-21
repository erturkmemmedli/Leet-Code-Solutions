class UndergroundSystem(object):
    def __init__(self):
        self.travel = {}
        self.customer = {}

    def checkIn(self, id, stationName, t):
        self.customer[id] = (stationName, t)  

    def checkOut(self, id, stationName, t):
        start = self.customer[id][0]
        time = t - self.customer[id][1]
        if (start, stationName) not in self.travel:
            self.travel[(start, stationName)] = (time, 1)
        else:
            period = self.travel[(start, stationName)][1]
            total = self.travel[(start, stationName)][0] * period
            self.travel[(start, stationName)] = ((total + time) / (period + 1), period + 1)

    def getAverageTime(self, startStation, endStation):
        return self.travel[(startStation, endStation)][0]
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)

# Alternative solution

from collections import defaultdict

class UndergroundSystem1:
    def __init__(self):
        self.customerRecordBook = {}
        self.flightTimeBook = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customerRecordBook[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        place, time = self.customerRecordBook[id]
        self.flightTimeBook[(place, stationName)].append((t - time))

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        result = self.flightTimeBook[(startStation, endStation)]
