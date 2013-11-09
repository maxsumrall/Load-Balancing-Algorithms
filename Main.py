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
    files = ["normal-3-1.txt","normal-6-2.txt","normal-100-30.txt","biNormal-100-300--30.txt", "biNormal-100-300--10.txt","pareto-1.txt","pareto-2.txt","pareto-3.txt","pareto-4.txt"]
    #files = ["pareto-1.txt","pareto-2.txt","pareto-3.txt","pareto-4.txt", "biNormal-100-300--30.txt", "biNormal-100-300--10.txt"]
    #files = ["biNormal-100-300--30.txt", "biNormal-100-300--10.txt"]
    machines = 20
    kLookAhead = 10
    writeIO = open('runTimes1.txt','w')
    writeIO.write("M = " + str(machines) + "K = " + str(kLookAhead) + "\n")
    for inputFile in files:
        writeIO.write("\n"+ inputFile + "\n----------------\n")
        print "\n"+ inputFile + "\n----------------"
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
        OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = OPT

    writeFile.write(" OPT: " + str(bestR)+"\n")
    print " OPT: " + str(bestR)

    writeFile.write("Sorted Greedy: \t\t" + str(bestS) + "|| Ratio: " + str(bestS/OPT)+ "\n")
    print "Sorted Greedy: \t\t" + str(bestS) + "|| Ratio: " + str(bestS/OPT)


    for i in range(5):
        bestM = 1
        bestS = 100000000000
        bestR = 1
        for m in  range(m,m+1):

            jobs = JobManager.JobManager(k,inputFile,m)
            machines = MachineBoss.MachineBoss(m)
            RandomScheduler.RandomScheduler(machines,jobs)


            makeSpan =  machines.maxMachine().makeSpan
            OPT = max(jobs.MAXJOB, jobs.sumJobTime/float(m))
            bestS,bestM = "",""
            if makeSpan < bestS:
                bestS = makeSpan
                bestM = m
                bestR = OPT
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    writeFile.write("RandomScheduler: \t " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)+"\n")
    print "RandomScheduler: \t " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for i in range(5):
        for m in  range(m,m+1):

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
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    writeFile.write("Random Search: \t\t " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)+"\n")
    print "Random Search: \t\t " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for i in range(5):
        for m in  range(m,m+1):

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
            #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
            #print "ratio: " + str(makeSpan/ratio)

    writeFile.write("RandomSearchStatistics:  " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)+"\n")
    print "RandomSearchStatistics:  " + str(bestS)+ "|| Ratio: " + str(bestS/OPT)


main()