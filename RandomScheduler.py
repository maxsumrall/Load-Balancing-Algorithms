__author__ = 'max'
import MachineBoss
import random
import time


class RandomScheduler:
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
            kJobs = (job[1][0])
            makesSpan=machines.maxMachine().getMakeSpan()+sum(kJobs)
            bestIndex=1
            for i in range(0,10):
                f_index = random.randint(0,len(machines.machines)-1)
                fakeMachines[f_index] += job[0]
                for kjob in kJobs:
                        index = random.randint(0,len(machines.machines)-1)
                        fakeMachines[index] += float(kjob)
                if(max(fakeMachines) < makesSpan):
                    makesSpan = max(fakeMachines)
                    bestIndex=f_index
            self.machines.machines[bestIndex].addJob(job[0])



