__author__ = 'max'

class Machine:
    def __init__(self):
        self.makeSpan = 0.0
        self.jobs = []
    def __str__(self):
        return str(self.makeSpan)
    def addJob(self,job):
        self.jobs.append(job)
        self.makeSpan += int(job.runTime)
    def getJobs(self):
        return self.jobs
    def getMakeSpan(self):
        return self.makeSpan