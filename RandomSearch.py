__author__ = 'max'
import MachineBoss
import time
import random
import math
class RandomSearch:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.bestMakeSpan = 100**10
        self.bestAssignment = [0,[]]

        for job in jobs:
            kNumberOfJobs = len(job[1])
            for trials in range(500):
                candidateAssignment = [0,[]]
                fakeMachines = []
                for m in machines.machines:
                    fakeMachines.append(m.makeSpan)
                candidateAssignment[0] = int(math.floor(random.uniform(0,self.machines.numberOfMachines))) #i-th element assignment

                for i in range(kNumberOfJobs):
                    randIndex = int(math.floor(random.uniform(0,self.machines.numberOfMachines)))
                    candidateAssignment[1].append(randIndex) #k element assignments
                #we've computed a random assignment and stored it in candidateAssignment

                fakeMachines[candidateAssignment[0]] += job[0]
                for i in range(kNumberOfJobs):
                    fakeMachines[candidateAssignment[1][i]] += job[1][i]

                if max(fakeMachines) < self.bestMakeSpan:
                    self.bestMakeSpan = max(fakeMachines)
                    self.bestAssignment = candidateAssignment

            #Found best assignemnt out of n-trials
            self.machines.machines[candidateAssignment[0]].addJob(job[0]) #and i-job to determined machine

