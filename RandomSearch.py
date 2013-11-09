__author__ = 'max'
import MachineBoss
import time
import random
import math
class RandomSearch:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.bestAssignment = [0,[]]

        for job in jobs:
            kNumberOfJobs = len(job[1])
            self.bestMakeSpan = 100**10
            for trials in range(len(self.machines.machines)*1):
                candidateAssignment = [0,[]]
                fakeMachines = []
                for m in machines.machines:
                    fakeMachines.append(m.makeSpan)

                candidateAssignment[0] = random.randint(0,self.machines.numberOfMachines-1) #i-th element assignment
                for i in range(kNumberOfJobs):
                    randIndex = random.randint(0,self.machines.numberOfMachines-1)
                    candidateAssignment[1].append(randIndex) #k element assignments
                    fakeMachines[candidateAssignment[1][i]] += job[1][i]
                fakeMachines[candidateAssignment[0]] += job[0]

                #we've computed a random assignment and stored it in candidateAssignment

                if max(fakeMachines) < self.bestMakeSpan:
                    self.bestMakeSpan = max(fakeMachines)
                    self.bestAssignment = list(candidateAssignment)

            #Found best assignemnt out of n-trials
            self.machines.machines[self.bestAssignment[0]].addJob(job[0]) #and i-job to determined machine

