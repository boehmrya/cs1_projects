

# Parses a line and extracts words from the line into a list. Any word that is
# extracted needs to be at least 4 letters long. Also, all extracted words are
# converted into all-lower-case before being inserted into the list.
def parse(s):
    listOfWords = [] # maintains the list of words in strings s
    currentWord = ""
    
    wordBeingProcessed = False
    
    i = 0 # serves as an index into the string s
    while i < len(s):
        # if the current character is a lower case letter
        if (s[i] >= "a" and s[i] <= "z"): 
            wordBeingProcessed = True
            currentWord = currentWord + s[i]
        # if the current character is an upper case character
        # do the same as above, except convert character into corresponding
        # lower case character using the ord() and chr() functions
        elif (s[i] >= "A" and s[i] <= "Z"):
            wordBeingProcessed = True
            currentWord = currentWord + chr(ord("a") + ord(s[i]) - ord("A"))
        # else if the current character is a non-letter
        # immediately following a word
        elif wordBeingProcessed:
            if len(currentWord) >= 4:
                listOfWords.append(currentWord)
            wordBeingProcessed = False
            currentWord = ""
        i = i + 1

    if wordBeingProcessed and len(currentWord) >= 4:
        listOfWords.append(currentWord)
            
    return listOfWords


# Searches for a word in wordList and returns the index of the first occurrence
# of word in wordList if found; otherwise returns -1.
def getIndex(wordList, word):
    # These are indices that keep track of the left
    # and right boundaries of the list that needs exploring
    left = 0
    right = len(wordList)-1
    
    # while left <= right, there is more to search
    while left <= right:
        middle = (left + right) // 2
        
        # Found k
        if word == wordList[middle]:
            return middle
        
        # If k is less than L[middle] search the 
        # left half
        if word < wordList[middle]:
            right = middle - 1
            
        # Otherwise search the right half
        elif word > wordList[middle]:
            left = middle + 1
        
    return left

# Takes a filename as parameter and parses the file, extracts words from the file
# and constructs two lists: one containing the words in the file and the other
# containing corresponding word-frequencies.
def computeWordFrequencies(filename):
    f = open(filename, "r")
    line = f.readline()
    masterDict = {} # for maintaining the list of words as keys, frequencies as values
    
    while line:
        wordsInLine = parse(line) # parse the current line to extract words
 
        index = 0
        while index < len(wordsInLine):
            # if word is already in masterList, increase its frequecy
            word = wordsInLine[index]
            if word in masterDict:
                masterDict[word] = masterDict[word] + 1
            else: # this is the first occurrence of the word, so just add key
                  # and set value (frequency) to 1
                masterDict[word] = 1
            index = index + 1
            
        line = f.readline()

    f.close()            
    return masterDict


