__author__ = 'max'
import MachineBoss
import JobManager
import GreedyScheduler
import SortedGreedyScheduler
import RandomScheduler

def main():
    k=3
    """
    for m in  range(2,4):

        jobs = JobManager.JobManager(k,'testFile.txt')
        machines = MachineBoss.MachineBoss(m)
        GreedyScheduler.GreedyScheduler(machines,jobs)

        makeSpan =  machines.maxMachine().makeSpan

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    LB = max(jobs.sumJobTime/m,max(jobs.jobs))
    print "LB = "+str(LB)
    print "Best: m= "+ str(m) + " Greedy makespan: " + str(makeSpan) + " ratio: " + str(makeSpan/LB)

    for m in  range(2,4):
        jobs = JobManager.JobManager(k,'testFile.txt')
        machines = MachineBoss.MachineBoss(m)
        SortedGreedyScheduler.SortedGreedyScheduler(machines,jobs)
        makeSpan =  machines.maxMachine().makeSpan

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
    print "Best: m= "+ str(m) + " SortedGreedy makespan: " + str(makeSpan) + " ratio: " + str(makeSpan/LB)
    for m in machines:
        print str(m.getJobs())
    """

    for m in  range(2,8):
        jobs = JobManager.JobManager(k,'input1.txt',m)
        machines = MachineBoss.MachineBoss(m)
        RandomScheduler.RandomScheduler(machines,jobs)
        makeSpan =  machines.maxMachine().makeSpan

        #print "Max Machine Run time: "+ str(makeSpan) + " OPT for " + str(m) + " machines is " + str(ratio)
        #print "ratio: " + str(makeSpan/ratio)
        LB = max(jobs.sumJobTime/m,max(jobs.jobs))
        print "LB = "+str(LB)
        print "Best: m= "+ str(m) + " Greedy makespan: " + str(makeSpan) + " ratio: " + str(makeSpan/LB)

main()