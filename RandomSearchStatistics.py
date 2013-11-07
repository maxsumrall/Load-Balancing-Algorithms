__author__ = 'max'
import MachineBoss
import time
import random
import math
class RandomSearchStatistics:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.bestMakeSpan = 100**10
        self.bestAssignment = [0,[]]

        for job in jobs:
            kNumberOfJobs = len(job[1])
            for trials in range(1000):
                candidateAssignment = [0,[]] #holds an int ofr each job where the int represents which machine to assign the job
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

            #have the best assignment be voted for in each job
            job[0].addVoteForIndex(candidateAssignment[0])
            for i in range(kNumberOfJobs):
                job[1][i].addVoteForIndex(candidateAssignment[1][i])


            #assign job i to its highest voted machine
            self.machines.machines[job[0].highestVotedIndex()].addJob(job[0])
