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
    k=10
    bestM = 1
    bestS = 100000000000
    bestR = 0
    inputFile = "input1.txt"

    for m in  range(20,21):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        GreedyScheduler.GreedyScheduler(machines,jobs)

        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/float(m)
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    print "Greedy: " + str(bestS) + " OPT: " + str(bestR)

    for m in  range(20,21):

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

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    print "Sorted Greedy: " + str(bestS)


    ###########

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        LeaveRoomSortedGreedy.LeaveRoomSortedGreedy(machines,jobs)
        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/float(m)
        LB = max(max(jobs.jobs),ratio)
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio
        print "Leave Room - Sorted Greedy: " + str(bestS)



#####

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

        jobs = JobManager.JobManager(k,inputFile,m)
        machines = MachineBoss.MachineBoss(m)
        HillClimbingScheduling.HillClimbingScheduling(machines,jobs)


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
    print "HillClimbing:  " + str(bestS)


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

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


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

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

    print "RandomScheduler:  " + str(bestS)

    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

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

    print "Random Search:  " + str(bestS)




main()