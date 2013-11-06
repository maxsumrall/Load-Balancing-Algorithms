__author__ = 'max'


class Job():
    def __init__(self,runtime,numberOfMachines):
        self.assignedMachines = []
        for i in range(numberOfMachines):
            self.assignedMachines.append(0)
        self.runTime = runtime

    def __str__(self):
        return self.runTime