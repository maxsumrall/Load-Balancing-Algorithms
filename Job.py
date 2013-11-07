__author__ = 'max'


class Job():
    def __init__(self,runtime,numberOfMachines):
        self.assignedMachines = []
        for i in range(numberOfMachines):
            self.assignedMachines.append(0)
        self.runTime = runtime

    def __str__(self):
        return str(self.runTime)

    def __get__(self):
        return self.runTime
    def __iter__(self):
        return self.runTime
    def __int__(self):
        return int(self.runTime)
    def __float__(self):
        return float(self.runTime)
    def __add__(self, other):
        return self.runTime + other
    def __radd__(self, other):
        return self.runTime + other
    def __cmp__(self, other):
        result = 0
        if self.runTime < other:
            result = -1
        if self.runTime > other:
            result = 1
        return result
    def __getattribute__(self, item):
        return self.runTime.index(item)

    def addVoteForIndex(self, votedIndex):
        self.assignedMachines[votedIndex] += 1

    def highestVotedIndex(self):
        return self.assignedMachines.index((max(self.assignedMachines)))