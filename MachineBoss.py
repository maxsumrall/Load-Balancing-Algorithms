__author__ = 'max'
import Machine

class MachineBoss:
    def __init__(self, numberOfMachines):
        self.numberOfMachines = numberOfMachines
        self.machines = []
        for i in range(numberOfMachines):
            self.machines.append(Machine.Machine())
        next = (i for i in self.machines)


    def __iter__(self):
        for i in self.machines:
            yield i

    def minMachine(self):
        minSize = self.machines[0]
        for i in self.machines:
           if minSize.getMakeSpan() > i.getMakeSpan():
               minSize = i
        return minSize

    def maxMachine(self):
        maxSize = self.machines[0]
        for i in self.machines:
           if maxSize.getMakeSpan() < i.getMakeSpan():
               maxSize = i
        return maxSize