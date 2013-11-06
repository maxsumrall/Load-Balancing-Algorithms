__author__ = 'max'
import MachineBoss
import time
class SortedGreedyScheduler:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs

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



