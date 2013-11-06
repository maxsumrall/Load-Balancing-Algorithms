__author__ = 'max'
import MachineBoss
import time
class GreedyScheduler:
    def __init__(self,machines,jobs):
        self.machines = machines
        self.jobs = jobs

        for job in jobs:
            machines.minMachine().addJob(job[0])



