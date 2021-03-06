import DistributionGenerator
import JobManager
import MachineBoss
import RandomScheduler
import SortedGreedyScheduler

__author__ = 'Nina'


class ExperimentWriter:
    Alg_SortedGreedy = 1
    Alg_Random = 2
    Algorithms = [Alg_SortedGreedy, Alg_Random]

    Distr_Normal = 1
    Distr_Pareto = 2
    Distributions = [Distr_Normal, Distr_Pareto]

    Sort_Sorted = 0
    Sort_Random = 1
    Sort_ReverseSorted = 2
    Sortings = [Sort_Sorted, Sort_Random, Sort_ReverseSorted]

    def WriteExperiment(self, Algorithm, Distribution, Sorting, k, m, JobsSizes=range(10, 1000)):
        #Check input data
        if not (Algorithm in self.Algorithms):
            raise ValueError("Please choose one of algorithms from ExperimentWriter class")

        if not (Distribution in self.Distributions):
            raise ValueError("Please choose one of distributions from ExperimentWriter class")

        if not (Sorting in self.Sortings):
            raise ValueError("Please choose one of sortings from ExperimentWriter class")

        Results = []
        #Generate jobs sets
        for j in JobsSizes:
            Jobs = []
            if Distribution == self.Distr_Normal:
                Jobs = DistributionGenerator.getGauss(j, 5)
            elif Distribution == self.Distr_Pareto:
                Jobs = DistributionGenerator.getPareto(j)

            #Sort input set
            if Sorting == self.Sort_Sorted:
                Jobs.sort()
            elif Sorting == self.Sort_ReverseSorted:
                Jobs.sort(reverse=True)

            fileName = "inputData" + str(j) + ".txt";
            tmpFile = open(fileName, 'w')
            for job in Jobs:
                tmpFile.write(str(job) + "\n")

            tmpFile.close()

            #Select scheduler
            #Scheduler = None
            Jobs = JobManager.JobManager(k, fileName, m)
            machines = MachineBoss.MachineBoss(m)

            if Algorithm == self.Alg_SortedGreedy:
                SortedGreedyScheduler.SortedGreedyScheduler(machines, Jobs)

            elif Algorithm == self.Alg_Random:
                RandomScheduler.RandomScheduler(machines, Jobs)

            makeSpan = machines.maxMachine().makeSpan
            #print makeSpan
            LB=max(Jobs.sumJobTime/float(m),max(Jobs.jobs))
            ratio = float(makeSpan)/float(LB)
            bestS, bestM = "", ""

            ResultsRow = []
            ResultsRow += [k]
            ResultsRow += [m]
            ResultsRow += [j]
            ResultsRow += [makeSpan]
            ResultsRow += [ratio]
            ResultsRow += [""]
            Results += [ResultsRow]


        writeResultsToCSV("TryMe.csv", Results)


def writeResultsToCSV(filename, resultsTable):
    import csv

    with open(filename, 'wb') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter.writerow(['k', 'm', 'JobsNum', 'MakeSpan', 'Ratio', 'Time'])
        for r in resultsTable:
            spamwriter.writerow(r)


Ex = ExperimentWriter()
Ex.WriteExperiment(ExperimentWriter.Alg_Random, ExperimentWriter.Distr_Pareto,
                   ExperimentWriter.Sort_ReverseSorted, 3, 6)