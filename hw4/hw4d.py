

def parse(s):
    wordList = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    start = 0
    current = 0
    count = 0

    while current < len(s):
        if s[current] in alphabet:
            count += 1
        else:
            if count >= 4:
                word = s[start:current]
                wordList.append(word.strip().lower())
            count = 0
            start = current
        current += 1

    return wordList



def computeWordFrequencies(filename):
     # list of list containing unique words in frequencies
     masterWordList = [[], []] 

     # open file, parse each line
     f = open(filename, 'r')
     s = f.read() # read the file into a string
     lines = s.split('\n')
     for line in lines:
          lineWords = parse(line)
          for word in lineWords:
               index = 0
               inList = False
               while index < len(masterWordList[0]):
                    # if the word is in the list, increment it's freq count
                    if masterWordList[0][index] == word:
                         masterWordList[1][index] += 1
                         inList = True
                         break
                    index += 1
               if inList == False: # if the word is not in list, add it to end
                    masterWordList[0].append(word)
                    masterWordList[1].append(1)
               else:
                    inList = False # reset                              
     f.close()
     return masterWordList



def mostFrequentWords(wordList, frequencyList, k):
     mostFreq = []
     freqIndex = []
     freqCount = 0
     threshold = 1000000
     while freqCount < k:
          maxFreq = 0
          maxIndex = 0
          index = 0
          while index < len(frequencyList):
               if frequencyList[index] > maxFreq and frequencyList[index] <= threshold:
                    if index not in freqIndex:
                         maxIndex = index
                         maxFreq = frequencyList[index]
               index += 1
          mostFreq.append(wordList[maxIndex])
          freqIndex.append(maxIndex)
          threshold = maxFreq
          freqCount += 1
     return mostFreq
          
                

def main():
    # number of most frequent words to process
    k = 20
    
    # process tolstoy first
    war = 'war.txt'
    masterWordList = computeWordFrequencies(war)
    wordList = masterWordList[0]
    frequencyList = masterWordList[1]
    tolstoyMostFrequent = mostFrequentWords(wordList, frequencyList, k)
    print("Tolstoy's 20 most frequent words are: ", tolstoyMostFrequent)

    # process stevenson second
    # start with hyde
    hyde = 'hyde.txt' 
    hydeWordList = computeWordFrequencies(hyde)
    hydeWords = hydeWordList[0]
    hydeFreq = hydeWordList[1]
    hydeMostFrequent = mostFrequentWords(hydeWords, hydeFreq, k)

    # then process treasure
    treasure = 'treasure.txt' 
    treasureWordList = computeWordFrequencies(treasure)
    treasureWords = treasureWordList[0]
    treasureFreq = treasureWordList[1]
    treasureMostFrequent = mostFrequentWords(treasureWords, treasureFreq, k)

    # then combine treasure and hyde for stevenson analysis
    steveTempWords = hydeWords + treasureWords
    steveTempFreq = hydeFreq + treasureFreq
    steveFinalWords = []
    steveFinalFreq = []
    index = 0
    while index < len(steveTempWords):
        # if the final word list has the current word
        # compare the frequencies and replace the old with the new if
        # the new words has a greater frequency
        if steveTempWords[index] in steveFinalWords:
            if steveTempFreq[index] > steveFinalFreq[index]:
                steveFinalWords[index] = steveTempWords[index]
                steveFinalFreq[index] = steveTempFreq[index]
        else:
            steveFinalWords.append(steveTempWords[index])
            steveFinalFreq.append(steveTempFreq[index])
        index += 1

    steveMostFrequent = mostFrequentWords(steveFinalWords, steveFinalFreq, k)
    print("Stevenson's 20 most frequent words are: ", steveFinalWords)
             
             
     
main()
