__author__ = 'max'
import MachineBoss
import time
import random
import math
class HillClimbingScheduling:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.bestMakeSpan = 100**10
        self.bestAssignment = [0,[]]

        for job in self.jobs:

            #1. Do Sorted Greedy to find a good solution
            #2. Do hill-climbing on our good solution to find a better solution

            kNumberOfJobs = len(job[1])
            sortedJobsBackwards = sorted(job[1]+[job[0]])
            sortedJobs = []
            #reverse jobs
            for i in sortedJobsBackwards[::-1]:
                sortedJobs.append(i)
            #


            candidateAssignment = [0,[]] #holds an int ofr each job where the int represents which machine to assign the job
            virtualAssignment = self.makeVirtualStateCopy()

            ithindex = 0
            for each in sortedJobs:
                minIndex = virtualAssignment.index(min(virtualAssignment))
                if (each.runTime > job[0].runTime):
                    candidateAssignment[1].append(minIndex)
                    virtualAssignment[minIndex] += each.runTime
                    ithindex+=1

            sortedJobs = sortedJobs[0:ithindex] + sortedJobs[ithindex+1:]
            minIndex = virtualAssignment.index(min(virtualAssignment))
            candidateAssignment[0] = minIndex
            virtualAssignment[minIndex] += job[0].runTime

            for each in sortedJobs:
                minIndex = virtualAssignment.index(min(virtualAssignment))
                if (each.runTime < job[0].runTime):
                    candidateAssignment[1].append(minIndex)
                    virtualAssignment[minIndex] += each.runTime



            #We've made candidateAssignment represent the sortedGreedy assignment of the variable sortedJobs

            if(kNumberOfJobs > 0):
                for iteration in range(0):
                    secondCandidate = [0,[]]
                    #secondCandidate[0] = candidateAssignment[0]
                    #for each in range(len(candidateAssignment[1])):
                    #    secondCandidate[1].append(candidateAssignment[1][each])
                    #if secondCandidate[1] == []:
                    #    secondCandidate[1] = [0]

                    #swapIndex1 = int(math.floor(random.uniform(0,len(secondCandidate[1]))))
                    #swapIndex2 = int(math.floor(random.uniform(0,len(secondCandidate[1]))))

                    #intermediary = secondCandidate[1][swapIndex1]
                    #secondCandidate[1][swapIndex1] = secondCandidate[1][swapIndex2]
                    #secondCandidate[1][swapIndex2] = intermediary

                    #print len(candidateAssignment[1]), len(secondCandidate[1])

                    secondCandidate[0] = int(math.floor(random.uniform(0,len(self.machines.machines))))
                    for each in range(len(candidateAssignment[1])):
                        secondCandidate[1].append(int(math.floor(random.uniform(0,len(self.machines.machines)))))



                    secondVirtualCopy = self.makeVirtualStateCopy()

                    secondVirtualCopy[secondCandidate[0]] += job[0]

                    for each in range(len(secondCandidate[1])):
                        secondVirtualCopy[secondCandidate[1][each]] += sortedJobs[each]

                    if max(secondVirtualCopy) < max(virtualAssignment):#new is better
                        #print "hill climbing worked!" + str(max(secondVirtualCopy)) + " vs " + str(max(virtualAssignment))
                        candidateAssignment[0] = secondCandidate[0]
                        for each in range(len(candidateAssignment[1])):
                            candidateAssignment[1][each] = secondCandidate[1][each]


            #candidateassignemtn should be the best of greedysorted plus the hill climbing
            self.machines.machines[candidateAssignment[0]].addJob(job[0])
            #for i in range(len(candidateAssignment[1])):
            #    self.machines.machines[candidateAssignment[i]] = sortedJobs[i]













    def makeVirtualStateCopy(self):
        va = []
        for m in self.machines.machines:
            va.append(m.getMakeSpan())
        return va