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

        #initilize fakemachines to represent the current state
        fakeMachines = []
        for m in machines.machines:
            fakeMachines.append(m.makeSpan)
        #do sorted-greedy
        for job in jobs:
            kNumberOfJobs = len(job[1])

            kJobs = (sorted(job[1])[0])
            kJobs.reverse()
            for kjob in kJobs:
                if(kjob > job[0]):
                    minIndex = fakeMachines.index(min(fakeMachines))
                    fakeMachines[minIndex] += float(kjob)
            #added kjobs > i-job
            fakeMachines[fakeMachines.index(min(fakeMachines))] += job[0]


            for trials in range(1000):
                candidateAssignment = [0,[]] #holds an int ofr each job where the int represents which machine to assign the job
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


        for job in jobs:
            #make new array of numbers, corresponding to size of machines workload ----fake machines------
            fakeMachines = []
            for m in machines.machines:
                fakeMachines.append(m.makeSpan)
            #order of makespans in fakeMachines corresponds to order of machines in self.machines
            #Now, add the k-jobs larger than our current i-job to our fake machines to determine where our i-job will really go
            kJobs = (sorted(job[1])[0])
            kJobs.reverse()
            #print kJobs
            #print job[0]
            for kjob in kJobs:
                if(kjob > job[0]):
                    minIndex = fakeMachines.index(min(fakeMachines))
                    fakeMachines[minIndex] += float(kjob)
            #        print "Job " + str(kjob) + " assigned to machine " + str(minIndex+1)
            #now all the bigger jobs are assigned to the correct machine.
            #we will get the index of the current min machine in a fake setup and assign the i-job to that machine IRL
            sortedGreedyIndex = fakeMachines.index(min(fakeMachines))
            self.machines.machines[sortedGreedyIndex].addJob(job[0])
            #print "ith job assigned to : " +str(sortedGreedyIndex+1)
            #print machines