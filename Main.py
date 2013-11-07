__author__ = 'max'
import MachineBoss
import JobManager
import GreedyScheduler
import SortedGreedyScheduler
import RandomScheduler
import RandomSearch
import RandomSearchStatistics
import HillClimbingScheduling

def main():
    k=50
    bestM = 1
    bestS = 100000000000
    bestR = 0

    for m in  range(20,21):

        jobs = JobManager.JobManager(k,'input1.txt',m)
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
    print "Best: m= "+ str(bestM) + " Greedy makespan: " + str(bestS) + " ratio: " + str(bestR)


    bestM = 1
    bestS = 100000000000
    bestR = 1
    for m in  range(20,21):

        jobs = JobManager.JobManager(k,'input1.txt',m)
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
    print "Best: m= "+ str(bestM) + " Random makespan: " + str(bestS) + " OPT: " + str(bestR)



main()