import preprocessdata as ppd

def calculateBiGramNoSmoothing(inputString1, wordList, twoWordList):
	Matrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] = twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			if words[i]+"-"+words[j] in twoWordList:
				ProbabilityMatrix[i][j] = float(twoWordList[words[i]+"-"+words[j]])/float(wordList[words[i]])

	print Matrix
	print ProbabilityMatrix




def main():
	stringToProcess = ppd.getStringFromFile()
	stringToProcess = ppd.stringCleanUp(stringToProcess)
	wordList,totalWords = ppd.getEachWordFrequency(stringToProcess)
	twoWordList = ppd.getGivenPreviousWordNewWordFrequency(stringToProcess)
	inputString1 = "The president has relinquished his control of the company's board"
	inputString2 = "The chief executive officer said the last year revenue was good"
	inputString1 = ppd.stringCleanUp(inputString1)
	inputString2 = ppd.stringCleanUp(inputString2)
	probability1 = calculateBiGramNoSmoothing(inputString1, wordList, twoWordList)
	probability2 = calculateBiGramNoSmoothing(inputString2, wordList, twoWordList)


if __name__ == '__main__':
	main()