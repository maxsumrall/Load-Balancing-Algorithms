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


	def generateInputFiles(self,Distribution, Sorting,JobsSizes=range(10, 1000)):
		if not (Distribution in self.Distributions):
			raise ValueError("Please choose one of distributions from ExperimentWriter class")

		if not (Sorting in self.Sortings):
			raise ValueError("Please choose one of sortings from ExperimentWriter class")
		FileNames=[]
		for j in JobsSizes:
			Jobs = []
			D=""
			S=""
			if Distribution == self.Distr_Normal:
				Jobs = DistributionGenerator.getGauss(j, 5)
				D="Normal distribution "
			elif Distribution == self.Distr_Pareto:
				Jobs = DistributionGenerator.getPareto(j)
				D="Pareto distribution "

			#Sort input set
			if Sorting == self.Sort_Sorted:
				Jobs.sort()
				S="sorted smallest to largest"
			elif Sorting == self.Sort_ReverseSorted:
				Jobs.sort(reverse=True)
				S="sorted largest to smallest"

			fileName="inputData"+str(j)+".txt";
			tmpFile=open(fileName,'w')
			tmpFile.write(D+S+"\n")
			for job in Jobs:
				tmpFile.write(str(job)+"\n")

			tmpFile.close()
			FileNames+=[fileName]
		return FileNames

	def WriteExperiment(self, Algorithm, k, m,inputFileNames,outputFileName):
		#Check input data
		if not (Algorithm in self.Algorithms):
			raise ValueError("Please choose one of algorithms from ExperimentWriter class")

		Results = []
		#Select scheduler
		Scheduler = None
		for fileName in inputFileNames:
			Jobs = JobManager.JobManager(k, fileName, m)
			machines = MachineBoss.MachineBoss(m)

			if Scheduler == self.Alg_SortedGreedy:
				Scheduler = SortedGreedyScheduler.SortedGreedyScheduler(machines, Jobs)

			elif Scheduler == self.Alg_Random:
				Scheduler = RandomScheduler.RandomScheduler(machines, Jobs)

			makeSpan = machines.maxMachine().makeSpan
			ratio = Jobs.sumJobTime / float(m)
			j=len(Jobs.jobs)
			bestS, bestM = "", ""

			ResultsRow = []
			ResultsRow += [k]
			ResultsRow += [m]
			ResultsRow += [j]
			ResultsRow += [makeSpan]
			ResultsRow += [ratio]
			ResultsRow += [""]
			Results += [ResultsRow]

		self.writeResultsToCSV(outputFileName, Results)


	def writeResultsToCSV(self, filename, resultsTable):
		import csv

		with open(filename, 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
			spamwriter.writerow(['k', 'm', 'JobsNum', 'MakeSpan', 'Ratio', 'Time'])
			for r in resultsTable:
				spamwriter.writerow(r)


Ex = ExperimentWriter()
inputFiles=Ex.generateInputFiles(ExperimentWriter.Distr_Pareto, ExperimentWriter.Sort_ReverseSorted)
Ex.WriteExperiment(ExperimentWriter.Alg_SortedGreedy, 3, 6,inputFiles,"tryMe.csv")