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

def main():
    files = ["normal.txt","input1.txt",'normal-3-1.txt','normal-6-2.txt,''normal-100-30.txt']
    machines = 20
    kLookAhead = 10
    writeIO = open('runTimes.txt','w')
    writeIO.write("M = " + str(machines) + "K = " + str(kLookAhead) + "\n")
    for inputFile in files:
        simpleTest(writeIO,inputFile,machines,kLookAhead)





def simpleTest(writeFile,inputFile,m,k):

    bestM = 1
    bestS = 100000000000
    bestR = 0




    for m in  range(m,m+1):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        SortedGreedyScheduler.SortedGreedyScheduler(machines,jobs)

        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/float(m)
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio

    writeFile.write(" OPT: " + str(bestR))

    writeFile.write("Sorted Greedy: \t\t" + str(bestS))


    for i in range(100):
        bestM = 1
        bestS = 100000000000
        bestR = 1
        for m in  range(m,m+1):

            jobs = JobManager.JobManager(k,inputFile,m)
            machines = MachineBoss.MachineBoss(m)
            RandomScheduler.RandomScheduler(machines,jobs)


            makeSpan =  machines.maxMachine().makeSpan
            ratio = jobs.sumJobTime/float(m)
            LB = max(max(jobs.jobs),ratio)
            bestS,bestM = "",""
            if makeSpan < bestS:
                bestS = makeSpan
                bestM = m
                bestR = ratio
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    writeFile.write("RandomScheduler: \t " + str(bestS))

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(m,m+1):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        RandomSearch.RandomSearch(machines,jobs)


        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/float(m)
        LB = max(max(jobs.jobs),ratio)
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio
        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)

    print "Random Search: \t\t " + str(bestS)


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(m,m+1):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        RandomSearchStatistics.RandomSearchStatistics(machines,jobs)


        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/float(m)
        LB = max(max(jobs.jobs),ratio)
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio
        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)

    print "RandomSearchStatistics:  " + str(bestS)


main()