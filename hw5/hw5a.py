

import time

# Two words are neighbors if they differ in exactly on letter.
# This function returns True if a given pair of words are neighbors
def areNeighbors(w1, w2):
     count = 0
     diffIndex = 0
     for i in range(len(w1)):
          if w1[i] != w2[i]:
               count = count + 1
               diffIndex = i
    
     if count == 1 and diffIndex > 1: # different letter is not the first
          return 1
     elif count == 1 and diffIndex == 1: # different letter is first, the rest same
          return 2
     else:
          return 0 # have more than one different letter, or same word

     

# The function reads from the file "words.dat" and inserts the words that are read
# into a list. The words are also inserted into a dictionary as keys, with each key 
# initialized to have [] as its value.
def readWords(wordList, D):
    fin = open("words.dat", "r")

    # Loop to read words from the and to insert them in a list
    # and in a dictionary
    for word in fin:
        newWord = word.strip("\n")
        wordList.append(newWord)
        D[newWord] = []

    fin.close()
    

# Builds the network of words using a dictionary. Two words are connected by an edge in this
# network if they are neighbors of each other, i.e., if they differ from each
# other in exactly one letter.
def buildDictionary(wordList, D):
     alpha = "abcdefghijklmnopqrstuvwxyz"

     # build word matrix - 26 empty lists
     wordMatrix = [] * 26
     for i in range(wordMatrix):
          wordMatrix[i] = []

     # build suffixes data structure, a list of length-2 lists
     suffixes = [] * 5,757
     for i in range(suffixes):
          suffixes[i] = []
          
     # Nested for loop to generate pairs of words
     for i in range(len(wordList)):
          for j in range(i+1, len(wordList)):
               # Check if the two generated words are neighbors
               # if so append word2 to word1's neighbor list and word1 to word2's neighbor list
               if areNeighbors(wordList[i], wordList[j]) == 1:
                    firstLetter = alpha.indexOf(wordList[i][0])
                    wordMatrix[firstLetter].append(wordList[i])
                    wordMatrix[firstLetter].append(wordList[j])
               elif areNeighbors(wordList[i], wordList[j]) == 2:
                    # first word
                    lastFourOne = wordList[i][1:] 
                    firstOne = wordList[i][0]
                    suffixes[i] = [lastFourOne, firstOne]
                    # second word
                    lastFourTwo = wordList[j][1:]
                    firstTwo = wordList[j][0]
                    suffixes[i] = [lastFourTwo, firstTwo]
                    
                    
                    
                    
    
# Explores the network of words D starting at the source word. If the exploration ends
# without reaching the target word, then there is no path between the source and the target.
# In this case the function returns False. Otherwise, there is a path and the function
# returns True.
def searchWordNetwork(source, target, D):

    # Initialization: processed and reached are two dictionaries that will help in the 
    # exploration. 
    # reached: contains all words that have been reached but not processed.
    # processed: contains all words that have been reached and processed, i.e., their neighbors have also been explored.
    # The values of keys are not useful at this stage of the program and so we use 0 as dummy values.
    processed = {source:0}
    reached = {}
    for e in D[source]:
        reached[e] = 0
       
    # Repeat until reached set becomes empty or target is reached 
    while reached:
        # Check if target is in reached; this would imply there is path from source to target
        if target in reached:
            return True
        
        # Pick an item in reached and process it
        item = reached.popitem() # returns an arbitrary key-value pair as a tuple
        newWord = item[0]
        
        # Find all neighbors of this item and add new neighbors to reached
        processed[newWord] = 0
        for neighbor in D[newWord]:
            if neighbor not in reached and neighbor not in processed:
                reached[neighbor] = 0 
    
    return False
        
# Main program
wordList = []
D = {}
readWords(wordList, D)
buildDictionary(wordList, D)

source = input("Please type the source word: ")
target = input("Please type the target word: ")

if searchWordNetwork(source, target, D):
    print("There is path from source to target")
else:
    print("There is no path from source to target")
