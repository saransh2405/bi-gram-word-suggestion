''' This file contains methods to process the data String,
	So as to remove anomilies like new line chars split sentences, remove initial and trailing spaces etc. '''


def removeNewLineChar(stringToProcess):
	return stringToProcess.replace("\n"," ");

def splitInLines(stringToProcess):
	return stringToProcess.replace(" . ",".\n");

def removeSpecialCharacter(stringToProcess):
	stringToProcess = stringToProcess.replace("'"," ").replace('"'," ").replace('-'," ");
	return stringToProcess