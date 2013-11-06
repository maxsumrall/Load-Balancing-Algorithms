__author__ = 'max'
import MachineBoss
import time
class RandomSearch:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.bestAssignment = ''
        for job in jobs:

            fakeMachines = []
                for m in machines.machines:
                    fakeMachines.append(m.makeSpan)


    def generateRandomAssignment:
        #return a random assignment of jobs to machines
        #return: generatedMakeSpan, assignmentMapping


    class virturalAssignment:
        def __init__(self,machines):
            self.makeSpan  = 0

