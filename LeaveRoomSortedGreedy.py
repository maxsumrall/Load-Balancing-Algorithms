__author__ = 'max'
import MachineBoss
import time
class LeaveRoomSortedGreedy:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs
        self.avg = 1
        for job in jobs:
            self.avg = (self.avg + job[0])/2.0
            #make new array of numbers, corresponding to size of machines workload ----fake machines------
            fakeMachines = []
            for m in machines.machines:
                fakeMachines.append(m.makeSpan)
            #order of makespans in fakeMachines corresponds to order of machines in self.machines
            #Now, add the k-jobs larger than our current i-job to our fake machines to determine where our i-job will really go
            kJobs = (sorted(job[1]))
            #kJobs.reverse()
            if kJobs == []:
                kJobs = [1]
            for kjob in kJobs[::-1]:
                if(kjob > job[0]):
                    if max(kJobs) > self.avg*(len(self.machines.machines)):
                        minIndex = self.indexOfSecondMin(fakeMachines)
                    else:
                        minIndex = fakeMachines.index(min(fakeMachines))
                    fakeMachines[minIndex] += float(kjob)

            #now all the bigger jobs are assigned to the correct machine.
            #we will get the index of the current min machine in a fake setup and assign the i-job to that machine IRL
            if max(kJobs) > self.avg*len(self.machines.machines):
                    sortedGreedyIndex = self.indexOfSecondMin(fakeMachines)
            else:
                    sortedGreedyIndex = fakeMachines.index(min(fakeMachines))
            sortedGreedyIndex = fakeMachines.index(min(fakeMachines))
            self.machines.machines[sortedGreedyIndex].addJob(job[0])
            #print "ith job assigned to : " +str(sortedGreedyIndex+1)
            #print machines


    def indexOfSecondMin(self,machinesToFindIn):
        minMachineVal = min(machinesToFindIn)
        secondMinVal = minMachineVal +1
        index = 0
        notFound = True
        while notFound:
            try:
                index = machinesToFindIn.index(int(secondMinVal))

                notFound = False#we found it
            except:
                if secondMinVal > max(machinesToFindIn):
                    notFound = False
                secondMinVal +=1

        return index
