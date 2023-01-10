from matplotlib import pyplot as plt
import random
import numpy as np

## function opens file and runs the algorithm 1000 and calls the histogram function
def experement():
    ## opens file
    wordFile = open("ww.txt", "r")

    ## creates array of lines
    lines = wordFile.readlines()

    ## counts the number of lines
    numberOfWords = len(lines)

    ## memory for the number of guess each time the algorithm is run
    guessArray = []

    for n in range(1000):
        guessArray.append(getGuessNumber(guessArray, numberOfWords, lines))

    histogram(guessArray)


## histogram function creats a histogram of the data
def histogram(guessArray):

    hist = np.histogram(guessArray)

    bins = []

    ## because the number of guess is varable the size ofthe the histogarm depends on the guesses
    for i in range(len(hist[0]) + 2):
        bins.append(i + 1)
     
    hist, bins = np.histogram(guessArray, bins)

    expectedValue(hist, bins)

    plt.hist(guessArray, bins)

    plt.title("Wordle strategy statistics")
    
    plt.show()

## expected value function calculates the expeced number of guesses
def expectedValue(hist, bins):
    expectedValue = 0

    ## sums the number of times the amount of guess occured multipyed by the weight of the guess
    for i in range(len(hist)):
        expectedValue += hist[i] * bins[i]

    ## then diveds by the probablty of the guess occuring
    expectedValue = expectedValue / 1000

    print("expected number of guesses = " + str(expectedValue))

    

def getGuessNumber(guessArray, numberOfWords, lines):
    
    ## generates a random number bettween 0 and the number of words in the file
    randomNumber = random.randrange(0, numberOfWords)

    ## selects a random word from the file
    randomWord = lines[randomNumber]

    ## creates an array of five zeros for the solution word
    solution = [0] * 5

    ## creates to empty arrays for the letters that are in the word and arnt in the word
    solutionLetter = []
    notSolutionLetter = []

    ## keeps track of the number of guess
    guessNumber = 0

    ## itterates through the hole list of words
    for line in lines:
        check = True

        ## itterates through the letters of each word
        for i in range(5):

            ## checks if the new word maches the postions of any found letters if not the word is not guessed
            if(solution[i] != 0 and line[i] != solution[i]):
                check = False
                break;

            ## checks if the word contains any letters that we know are not in the final solution if there is the word is not guessed
            if(line[i] in notSolutionLetter):
                check = False
                break;

        ## checks if the word contains all the letters we know will be in the final solution if not the word is not guessed
        for k in range(len(solutionLetter)):

            if(solutionLetter[k] not in line):
                check = False
                break;

        ## checks if we passed all guess conditions
        if check == True:

            check = False

            ## itterates through all the letters of the word again
            for j in range(5):

                ## commits the letters of the word guessed to memory if statment makes sure there arnt duplicate letters
                if(line[j] not in solutionLetter and line[j] not in notSolutionLetter):
                    check = True
                    if line[j] in randomWord:
                        solutionLetter.append(line[j])
                    else:
                        notSolutionLetter.append(line[j])

                ## if postitions saves them to memory
                if(line[j] == randomWord[j]):
                    solution[j] = line[j]
        

        ## adds a guess to the count
        if(check == True):
            guessNumber += 1

        ## checks if we found soltion my making sure all zeros are gone
        if(0 not in solution):
            break

    return guessNumber

## calls all other functions
def main():
    experement()

main()


