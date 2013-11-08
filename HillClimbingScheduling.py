__author__ = 'max'
import MachineBoss
import time
import random
import math
class HillClimbingScheduling:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs

        for job in self.jobs:

            #1. Do Sorted Greedy to find a good solution
            #2. Do hill-climbing on our good solution to find a better solution

            self.bestAssignment = [0,[]]
            self.bestMakeSpan = 100**10
            kNumberOfJobs = len(job[1])
            sortedJobsBackwards = sorted(job[1]+[job[0]])
            sortedJobs = []
            #reverse jobs
            for i in sortedJobsBackwards[::-1]:
                sortedJobs.append(i)
            #


            virtualMachineState = self.makeVirtualStateCopy()

            ithindex = 0
            for each in sortedJobs:
                minIndex = virtualMachineState.index(min(virtualMachineState))
                if (each.runTime > job[0].runTime):
                    self.bestAssignment[1].append(int(minIndex))
                    virtualMachineState[minIndex] += int(each.runTime)
                    ithindex+=1

            sortedJobs = sortedJobs[0:ithindex] + sortedJobs[ithindex+1:]
            minIndex = virtualMachineState.index(min(virtualMachineState))
            self.bestAssignment[0] = int(minIndex)
            virtualMachineState[minIndex] += int(job[0].runTime)

            for each in sortedJobs:
                minIndex = virtualMachineState.index(min(virtualMachineState))
                if (each.runTime < job[0].runTime):
                    self.bestAssignment[1].append(int(minIndex))
                    virtualMachineState[minIndex] += int(each.runTime)



            #We've made candidateAssignment represent the sortedGreedy assignment of the variable sortedJobs

            if(kNumberOfJobs > 0):
                for iteration in range(len(self.machines.machines)*100):

                    secondCandidate = list(self.bestAssignment)
                    secondVirtualCopy = self.makeVirtualStateCopy()
                    hillClimb = True
                    randomSearch = True

                    if hillClimb:
                        secondCandidate = list(self.bestAssignment)

                        swapIndex1 = random.randint(0,len(secondCandidate[1])-1)
                        swapIndex2 = random.randint(0,len(secondCandidate[1])-1)

                        intermediary = int(secondCandidate[1][swapIndex1])
                        secondCandidate[1][swapIndex1] = int(secondCandidate[1][swapIndex2])
                        secondCandidate[1][swapIndex2] = int(intermediary)

########################################
                    elif randomSearch:
                        secondCandidate[0] = int(math.floor(random.uniform(0,len(self.machines.machines))))
                        for each in range(len(secondCandidate[1])):
                            secondCandidate[1].append(int(math.floor(random.uniform(0,len(self.machines.machines)))))
########################################
                    secondVirtualCopy[secondCandidate[0]] += int(job[0].runTime)
                    for each in range(len(secondCandidate[1])):
                        secondVirtualCopy[secondCandidate[1][each]] += int(sortedJobs[each].runTime)

                    if max(secondVirtualCopy) < max(virtualMachineState):#new is better
                       # print "hill climbing worked!" + str(max(secondVirtualCopy)) + " vs " + str(max(virtualAssignment))
                       # print swapIndex1, swapIndex2
                       # for each in range(len(secondCandidate[1])):
                       #     print str(secondCandidate[1][each]) + " : " + str(candidateAssignment[1][each])
                       # raw_input()
                        self.bestAssignment = list(secondCandidate)


            #candidateassignemtn should be the best of greedysorted plus the hill climbing
            self.machines.machines[self.bestAssignment[0]].addJob(job[0])
            #for i in range(len(candidateAssignment[1])):
            #    self.machines.machines[candidateAssignment[i]] = sortedJobs[i]













    def makeVirtualStateCopy(self):
        va = []
        for m in self.machines.machines:
            va.append(m.getMakeSpan())
        return va