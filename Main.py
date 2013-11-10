__author__ = 'max'
import MachineBoss
import JobManager
import GreedyScheduler
import SortedGreedyScheduler
import RandomScheduler
import RandomSearch
import RandomSearchStatistics
import HillClimbingScheduling
import LeaveRoomSortedGreedy
import time

def main():
    files = ["normal-3-1.txt","normal-6-2.txt","normal-100-30.txt","biNormal-100-300--30.txt", "biNormal-100-300--10.txt","pareto-1.txt","pareto-2.txt","pareto-3.txt","pareto-4.txt"]
    #files = ["pareto-1.txt","pareto-2.txt","pareto-3.txt","pareto-4.txt", "biNormal-100-300--30.txt", "biNormal-100-300--10.txt"]
    #files = ["biNormal-100-300--30.txt", "biNormal-100-300--10.txt"]
    machines = 5
    kLookAhead = 5
    mStep = [5,10,15,20,25,30]
    kStep = [5,10,15,20,25,30]
    writeIO = open('pareto-1-MStep.csv','w')
    writeIO.write("M,K,Sorted Greedy,Random Search, Random Search with History \n")
    for variable in mStep:
        #writeIO.write("\n"+ inputFile + "\n----------------\n")
        #print "\n"+ inputFile + "\n----------------"
        simpleTest(writeIO,files[5],variable,kStep[0])
    #randomRetries(files[3],machines,kLookAhead)



def randomRetries(inputFile,m,k):

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for i in range(5):
        for m in  range(m,m+1):
            startTime = time.time()
            jobs = JobManager.JobManager(k,inputFile,m)
            machines = MachineBoss.MachineBoss(m)
            RandomSearch.RandomSearch(machines,jobs)


            makeSpan =  machines.maxMachine().makeSpan
            OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
            bestS,bestM = "",""
            if makeSpan < bestS:
                bestS = makeSpan
                bestM = m
                bestR = OPT
            exTime = time.time() - startTime
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

        print "Random Search: \t\t " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)+ " run time: " + str(exTime)

def simpleTest(writeFile,inputFile,m,k):
    line = ""
    bestM = 1
    bestS = 100000000000
    bestR = 0
    for m in  range(m,m+1):
        startTime = time.time()
        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        SortedGreedyScheduler.SortedGreedyScheduler(machines,jobs)

        makeSpan =  machines.maxMachine().makeSpan
        OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = OPT
        exTime = time.time() - startTime


    line = line + str(m)+","+str(k)+","+str(bestS/OPT) + ","


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for i in range(5):
        for m in  range(m,m+1):
            startTime = time.time()
            jobs = JobManager.JobManager(k,inputFile,m)
            machines = MachineBoss.MachineBoss(m)
            RandomSearch.RandomSearch(machines,jobs)


            makeSpan =  machines.maxMachine().makeSpan
            OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
            bestS,bestM = "",""
            if makeSpan < bestS:
                bestS = makeSpan
                bestM = m
                bestR = OPT
            exTime = time.time() - startTime
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    line = line + str(bestS/OPT) +","


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for i in range(5):
        for m in  range(m,m+1):
            startTime = time.time()
            jobs = JobManager.JobManager(k,inputFile,m)
            machines = MachineBoss.MachineBoss(m)
            RandomSearchStatistics.RandomSearchStatistics(machines,jobs)


            makeSpan =  machines.maxMachine().makeSpan
            OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
            bestS,bestM = "",""
            if makeSpan < bestS:
                bestS = makeSpan
                bestM = m
                bestR = OPT
            exTime = time.time() - startTime
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    line = line+ str(bestS/OPT) + "\n"
    writeFile.write(line)


main()