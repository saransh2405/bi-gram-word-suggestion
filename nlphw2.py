import preprocessdata as ppd

def printArray(array):
	for each in array:
		print each

def calculateBiGramNoSmoothing(inputString1, wordList, twoWordList):
	Matrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] = twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i] in wordList:
				dividedby[i][j] = wordList[words[i]]

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			if dividedby[i][j] != 0:
				ProbabilityMatrix[i][j] = float(Matrix[i][j])/float(dividedby[i][j])
			else:
				ProbabilityMatrix[i][j] = 0

	print '------------------------------- Matrix ----------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)


def calculateBiGramWithSmoothing(inputString1, wordList, twoWordList, totalWords):
	Matrix = [[1 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] += twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i] in wordList:
				dividedby[i][j] = wordList[words[i]]+totalWords

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			ProbabilityMatrix[i][j] = float(Matrix[i][j])/float(dividedby[i][j])

	print '------------------------------- Matrix ----------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)




def main():
	stringToProcess = ppd.getStringFromFile()
	stringToProcess = ppd.stringCleanUp(stringToProcess)
	wordList,totalWords = ppd.getEachWordFrequency(stringToProcess)
	twoWordList = ppd.getGivenPreviousWordNewWordFrequency(stringToProcess)
	inputString1 = "The president has relinquished his control of the company's board"
	inputString2 = "The chief executive officer said the last year revenue was good hubahuba hurrr"
	inputString1 = ppd.stringCleanUp(inputString1)
	inputString2 = ppd.stringCleanUp(inputString2)

	''' here we calculate the probability tables without any smoothing technique'''
	probability1 = calculateBiGramNoSmoothing(inputString1, wordList, twoWordList)
	#probability2 = calculateBiGramNoSmoothing(inputString2, wordList, twoWordList)


	''' add one smoothing technique '''
	probability1 = calculateBiGramWithSmoothing(inputString1, wordList, twoWordList, totalWords)
	#probability2 = calculateBiGramWithSmoothing(inputString2, wordList, twoWordList, totalWords)

	print totalWords




if __name__ == '__main__':
	main()