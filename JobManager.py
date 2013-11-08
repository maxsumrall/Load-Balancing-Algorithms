__author__ = 'max'
import Job
#aka the GOD file. Ask God for a job, he retuns the next job.

class JobManager:
    def __init__(self, kLookAhead, inputFile, numberOfMachines):
        self.numberOfMachines = numberOfMachines
        self.readFile = open(inputFile, 'r')
        self.jobs = []
        self.lookAhead = kLookAhead
        self.sumJobTime = 0.0
        line = self.readFile.readline()
        self.jobs = self.readFile.readlines()
        self.readFile.close()
        for i in range(len(self.jobs)):
            self.jobs[i] = Job.Job(int(float(self.jobs[i].replace('\n', ''))), self.numberOfMachines)
            self.sumJobTime += float(self.jobs[i])
        self.MAXJOB = Job.Job(0, self.numberOfMachines)


    def __str__(self):
        output = ""
        for each in self.jobs:
            output += ", " + str(each)
        return str(output)


    def __iter__(self):
        for i in range(len(self.jobs)):
            work = []
            futureWork = []
            work.append(self.jobs[i])
            futureWork.append(self.jobs[i + 1:i + 1 + self.lookAhead])

            yield work[0], futureWork[0]


    def __getitem__(self, item):
        return int(self.jobs[item])

