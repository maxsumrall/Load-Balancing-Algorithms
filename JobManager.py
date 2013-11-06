__author__ = 'max'
#aka the GOD file. Ask God for a job, he retuns the next job.

class JobManager:
    def __init__(self,kLookAhead,inputFile):
        self.readFile = open(inputFile,'r')
        self.jobs = []
        self.lookAhead = kLookAhead
        self.sumJobTime = 0.0
        line = self.readFile.readline()
        self.jobs = self.readFile.readlines()
        self.readFile.close()
        for i in range(len(self.jobs)):
            self.jobs[i] = self.jobs[i].replace('\n','')
            self.sumJobTime += float(self.jobs[i])

    def __str__(self):
        print self.jobs

    def __iter__(self):
        for i in range(len(self.jobs)):
            work = []
            futureWork = []
            work.append(self.jobs[i])
            futureWork.append(self.jobs[i+1:i+1+self.lookAhead])

            yield work[0],futureWork
