__author__ = 'max'
import MachineBoss
import JobManager
import GreedyScheduler
import SortedGreedyScheduler

def main():
    k=10
    bestM = 1
    bestS = 100000000000
    bestR = 0
    for m in  range(2,3):

        jobs = JobManager.JobManager(k,'increasing.txt')
        machines = MachineBoss.MachineBoss(m)
        GreedyScheduler.GreedyScheduler(machines,jobs)


        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/m
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    print "Best: m= "+ str(bestM) + " Greedy makespan: " + str(bestS) + " ratio: " + str(bestR)


    bestS = 100000000000

    for m in  range(2,3):

        jobs = JobManager.JobManager(k,'increasing.txt')
        machines = MachineBoss.MachineBoss(m)
        SortedGreedyScheduler.SortedGreedyScheduler(machines,jobs)


        makeSpan =  machines.maxMachine().makeSpan
        ratio = jobs.sumJobTime/m
        bestS,bestM = "",""
        if makeSpan < bestS:
            bestS = makeSpan
            bestM = m
            bestR = ratio
        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    print "Best: m= "+ str(bestM) + " SortedGreedy makespan: " + str(bestS) + " ratio: " + str(bestR)





main()