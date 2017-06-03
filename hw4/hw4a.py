

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
                
        


def test():
    s = "Lincoln's silly, flat and dishwatery utterances - Chicago Times, 1863"
    wordList = parse(s)
    print(wordList)


test()    
