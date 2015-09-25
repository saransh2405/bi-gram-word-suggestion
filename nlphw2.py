import preprocessdata as ppd

def printArray(array):
	for each in array:
		print each

def sentenceProbability(words, twoWordList, probMatrix):
	probability = 1
	for i in range(0,len(words) - 1):
		probability *= probMatrix[i][i+1]

	return probability


def calculateBiGramNoSmoothing(inputString1, wordList, twoWordList, totalSentences):
	print "For the sentence",inputString1,"using bigrams no smothing technique"
	Matrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	probability = 0

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

	if "-"+words[0] in twoWordList:
		probability = float(float(twoWordList["-"+words[0]]))/float(totalSentences)


	print '------------------------------- Matrix -----------------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)
	print '------------------------------- SentenceProbability ----------------------------'
	probability *= sentenceProbability(words, twoWordList, ProbabilityMatrix)

	return probability


def calculateBiGramWithSmoothing(inputString1, wordList, twoWordList, totalWords, totalSentences):
	print "For the sentence",inputString1,"using bigrams with smothing technique - Add one"
	Matrix = [[1 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	probability = 0

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] += twoWordList[words[i]+"-"+words[j]]

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i] in wordList:
				dividedby[i][j] = wordList[words[i]]+totalWords
			else:
				dividedby[i][j] = totalWords

	for i in range(0,len(ProbabilityMatrix)):
		for j in range(0,len(ProbabilityMatrix)):
			ProbabilityMatrix[i][j] = float(Matrix[i][j])/float(dividedby[i][j])

	if "-"+words[0] in twoWordList:
		probability = float(float(twoWordList["-"+words[0]]+1))/float(totalSentences+totalWords)


	print '------------------------------- Matrix ----------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)
	print '------------------------------- SentenceProbability ----------------------------'
	probability *= sentenceProbability(words, twoWordList, ProbabilityMatrix)

	return probability



def calculateGoodTuringTechnique(inputString1, wordList, twoWordList, totalWords, totalSentences):
	print "For the sentence",inputString1,"using bigrams no smothing technique - good-turing"
	Matrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	ProbabilityMatrix = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	dividedby = [[0 for x in range(len(inputString1.split()))] for x in range(len(inputString1.split()))]
	probability = 0

	words = inputString1.split()
	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if words[i]+"-"+words[j] in twoWordList:
				Matrix[i][j] = twoWordList[words[i]+"-"+words[j]]
	
	NC = [0,0,0,0,0,0,0]
	cstar = [0,0,0,0,0,0]
	N = 0
	
	for each in twoWordList:
		N += twoWordList[each]
		if twoWordList[each] < 7:
			NC[twoWordList[each]] += 1
	
	NC[0] = 0
	cstar[0] = float(NC[1])/N

	''' taking k = 5 '''
	k = 5
	for c in range(1,6):
		cstar[c] = (((c+1)*(float(NC[c+1])/NC[c]) - c*(k+1)*float(NC[k+1])/NC[1])/(1 - (k+1)*float(NC[k+1])/NC[1]))/N

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

	for i in range(0,len(Matrix)):
		for j in range(0,len(Matrix)):
			if Matrix[i][j] < 6:
				ProbabilityMatrix[i][j] = cstar[Matrix[i][j]]
			else:
				ProbabilityMatrix[i][j] = ProbabilityMatrix[i][j]

	if "-"+words[0] in twoWordList:
		if twoWordList["-"+words[0]] < 6:
			probability = cstar[twoWordList["-"+words[0]]]
		else:
			probability = float(float(twoWordList["-"+words[0]]))/float(totalSentences)
	else:
		probability = cstar[0]


	print '------------------------------- Matrix -----------------------------------------'
	printArray(Matrix)
	print '------------------------------- ProbabilityMatrix ------------------------------'
	printArray(ProbabilityMatrix)
	print '------------------------------- SentenceProbability ----------------------------'
	probability *= sentenceProbability(words, twoWordList, ProbabilityMatrix)

	return probability



	


def main():
	stringToProcess = ppd.getStringFromFile()
	stringToProcess = ppd.stringCleanUp(stringToProcess)
	wordList, totalWords, totalSentences = ppd.getEachWordFrequency(stringToProcess)
	twoWordList = ppd.getGivenPreviousWordNewWordFrequency(stringToProcess)
	inputString1 = "The president has relinquished his control of the company's board"
	inputString2 = "The chief executive officer said the last year revenue was good"
	inputString1 = ppd.stringCleanUp(inputString1)
	inputString2 = ppd.stringCleanUp(inputString2)

	''' here we calculate the probability tables without any smoothing technique'''
	probability1 = calculateBiGramNoSmoothing(inputString1, wordList, twoWordList, totalSentences)
	print "Probability of sentence 1 is", probability1,
	print "\n\n\n"
	probability2 = calculateBiGramNoSmoothing(inputString2, wordList, twoWordList, totalSentences)

	print "Probability of sentence 1 is", probability1,"Probability of sentence 2 is", probability2
	print "\n\n\n"

	''' add one smoothing technique '''
	probability1 = calculateBiGramWithSmoothing(inputString1, wordList, twoWordList, totalWords, totalSentences)
	print "Probability of sentence 1 is", probability1,
	print "\n\n\n"
	probability2 = calculateBiGramWithSmoothing(inputString2, wordList, twoWordList, totalWords, totalSentences)

	print "Probability of sentence 1 is", probability1,"Probability of sentence 2 is", probability2
	print "\n\n\n"

	''' good-turing technique '''
	probability1 = calculateGoodTuringTechnique(inputString1, wordList, twoWordList, totalWords, totalSentences)
	print "Probability of sentence 1 is", probability1,
	print "\n\n\n"
	probability2 = calculateGoodTuringTechnique(inputString2, wordList, twoWordList, totalWords, totalSentences)

	print "Probability of sentence 1 is", probability1,"Probability of sentence 2 is", probability2





if __name__ == '__main__':
	main()