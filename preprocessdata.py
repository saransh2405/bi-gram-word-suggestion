''' This file contains methods to process the data String,
	So as to remove anomilies like new line chars split sentences, remove initial and trailing spaces etc. '''


import re

def removeNewLineChar(stringToProcess):
	return stringToProcess.replace("\n"," ")

def splitInLines(stringToProcess):
	return stringToProcess.replace(" . ","\n")

def removeSpecialCharacter(stringToProcess):
	stringToProcess = stringToProcess.replace(" '","'").replace('"'," ").replace('-'," ").replace("`"," ")
	stringToProcess = stringToProcess.replace(","," ").replace("\\"," ").replace("/"," ").lower()
	stringToProcess = re.sub(' +',' ',stringToProcess)
	return stringToProcess

def removeTrailingSpaces(stringToProcess):
	stringList = stringToProcess.split("\n")
	stringToProcess = ""
	for each in stringList:
		stringToProcess += each.strip()+"\n"
	return stringToProcess

def getStringFromFile():
	data = ""
	with open("corpus.txt", "r+") as f:
		data = f.read()
	return data

def getEachWordFrequency(stringToProcess):
	stringList = stringToProcess.split("\n")
	wordList = {}
	totalWords = 0
	for each in stringList:
		lineWords = each.strip().split()
		for eachWord in lineWords:
			totalWords += 1
			if eachWord in wordList:
				wordList[eachWord] += 1
			else:
				wordList[eachWord] = 1

	return wordList,totalWords

def getGivenPreviousWordNewWordFrequency(stringToProcess):
	stringList = stringToProcess.split("\n")
	wordList = {}
	totalWords = 0
	for each in stringList:
		lineWords = each.strip().split()
		for i in range(0,len(lineWords)):
			if i == 0:
				if "-"+lineWords[i] in wordList:
					wordList["-"+lineWords[i]] += 1
				else:
					wordList["-"+lineWords[i]] = 1
			else:
				key = lineWords[i-1]+"-"+lineWords[i]
				if key in wordList:
					wordList[key] += 1
				else:
					wordList.update({key : 1})
	return wordList

def stringCleanUp(stringToProcess):
	stringToProcess = removeNewLineChar(stringToProcess)
	stringToProcess = splitInLines(stringToProcess)
	stringToProcess = removeSpecialCharacter(stringToProcess)
	stringToProcess = removeTrailingSpaces(stringToProcess)
	return stringToProcess