__author__ = 'natalia'
import MachineBoss
import random
import time


class RandomScheduler:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs

        for job in jobs:
            kJobs = (job[1])
            makesSpan=machines.maxMachine().getMakeSpan()+sum(kJobs)
            bestIndex=1
            #print "Current is "
            #print machines.machines
            #print str(machines)
            for i in range(0,len(machines.machines)*100):
                fakeMachines=[]
                for m in machines.machines:
                    fakeMachines.append(m.makeSpan)
                f_index = random.randint(0,len(machines.machines)-1)
                fakeMachines[f_index] += job[0]
                for kjob in kJobs:
                        index = random.randint(0,len(machines.machines)-1)
                        fakeMachines[index] += float(kjob)
                        if(max(fakeMachines) >  makesSpan):
                            break
                #print fakeMachines
                if(max(fakeMachines) < makesSpan):
                    makesSpan = max(fakeMachines)
                    bestIndex=f_index
                    #print "better"
                    #print fakeMachines
            self.machines.machines[bestIndex].addJob(job[0])
        #print str(machines)
            #print "Best makeSpan is "
            #print makesSpan


