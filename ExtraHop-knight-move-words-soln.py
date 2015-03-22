# Author: Ly Nguyen
# Location: Seattle, WA
# LinkedIn: www.linkedin.com/in/lynguyen60

#Thoughts: 
# We should not produce really really long words.
# The run time will last O(4 legal moves ^ longest word length)
# which is exponential run time. We can optimize by pruning
# paths of candidate words by checking to see whether
# the candidate so far has any matching words in the text.
# I.e., if the current candidate word is "cand" and ("candy",
# "candidate") are words in the text, it will keep moving
# to the next legal-knight move. However if the next letter
# is "a", making the word "canda", stop search from this
# "a" branch. Go back to "d" and start with the next legal
# move from there. Whenever we get a candidate word that matches
# a word in the text, we add it to our list of results. We
# keep going down that path until we run out of words in text
# that match our candidate word so far, and then retract.
# We can do this recursively, so that we compare our candidate
# words to only words in text that match the candidate so far.


import sys
import re
import argparse

# parse arguments
parser = argparse.ArgumentParser(description='Return longest word from text found when traversing a matrix with legal Chess Knight moves. Ex: python ExtraHop-knight-move-words-soln.py ExtraHop-Loves-Labours-Lost.txt ExtraHop-matrix.txt 2 2')
parser.add_argument('textfile',
                   help='name of text file to test candidate words against')
parser.add_argument('matrixfile',
                   help='name of text file containg 8 rows with 8 characters in each row')
parser.add_argument('y', type=int,
                   help='number that represents starting y coordinate, base-0')
parser.add_argument('x', type=int,
                   help='number that represents starting x coordinate, base-0')

args = parser.parse_args()


# globals
MATRIX_LENGTH = 8
MOVES = [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]

# next possible coordinates from these coordinates
def getNextCoords(y,x):
	nextCoords = []
	for move in MOVES:
		nextCoord = (y + move[1], x + move[0]) 
		if nextCoord[0] < MATRIX_LENGTH and nextCoord[1] < MATRIX_LENGTH:
			nextCoords.append(nextCoord)
	return nextCoords

# read file and create set of pre-processed words
def createWordSet(fileName):
	print fileName
	fileT = open(fileName, 'r')
	setWords = set()

	# split into words, strip, add to set
	for line in fileT:
		for word in line.split(' '):
			word = preprocessWord(word)
			if not word == '':
				setWords.add(word)

	fileT.close()
	return setWords

# strip words of punctuation and return lowercase
def preprocessWord(word):
	# strips punctuation from word
	word = re.sub(r'[^a-zA-Z0-9]', r'', word)

	# convert to lowercase
	word = word.lower()

	return word

# read file and create nested list of characters
def createLetterMatrix(fileName):
	fileM = open(fileName, 'r')
	matrix = [[0 for x in range(8)] for x in range(8)] 

	# expects 8x8, handle errors
	y = 0
	for line in fileM:
		if y > MATRIX_LENGTH: 
			sys.exit("There are more rows of letters than allowed") 
		x = 0
		for char in line.split(' '):
			if x > MATRIX_LENGTH:
				sys.exit("There are more columns of letters than allowed") 
			matrix[y][x] = preprocessWord(char)
			x += 1
		y += 1

	fileM.close()
	return matrix

# remove word from set if "char" is not at position "position" in the word
def filterWords(setWords, position, char):
	tempList = []
	for word in setWords:
		if len(word) > position:
			if word[position] == char:
				tempList.append(word)
	return set(tempList)

# recursive: return words found when traversing from these coordinates
def recGetMatches(charPosition, setWords, curY, curX, curStr, matrix):
	matches = []

	# reduce setWords to the letter at current position
	startLetter = matrix[curY][curX]
	setWords = filterWords(setWords, charPosition, startLetter)

	# BASECASE: if no words in setWords have this letter in this position, prune path
	if len(setWords) == 0:
		return matches

	# add this letter to curStr and validate if it's a full word in setWords
	curStr += startLetter
	if curStr in setWords:
		matches.append(curStr)

	# do this for 8 next possible moves
	nextCoords = getNextCoords(curY, curX)
	for y,x in nextCoords:
		matches += recGetMatches(charPosition+1, setWords, y, x, curStr, matrix)

	return matches


if __name__ == "__main__":
	wordSet = createWordSet(args.textfile)
	letterMatrix = createLetterMatrix(args.matrixfile)
	y = args.y
	x = args.x

	# get candidate words that exist in the wordSet
	matches = recGetMatches(0, wordSet, y, x, "", letterMatrix)

	# find longest matched word
	if len(matches) > 0:
		longestLengthIdx = 0
		for idx, word in enumerate(matches):
			if len(word) > len(matches[longestLengthIdx]):
				longestLengthIdx =  idx
		print "First longest word found: ", matches[longestLengthIdx]
	else:
		print "No words found"
