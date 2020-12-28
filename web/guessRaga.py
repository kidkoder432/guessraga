def tri(n): #triangular number calculator
    t = 0
    for i in range(n):
        t += i
    return t
def loadDictionary(): # open raga database
    dictionaryFile = open("saptaks.txt")
    englishWords = {}
    for word in dictionaryFile.read().split('\n'):
        englishWords[word] = 0
    dictionaryFile.close()
    return englishWords    
def getRagaCount(message): # guessing code
    p = []
    SAPTAKS = loadDictionary()
    for x in range(2, len(message) - 1):
        for i in range(len(message) - x + 1):
            for saptak in list(SAPTAKS.keys()):
                if ''.join(message[i:i + x]) in saptak:
                    SAPTAKS[saptak] += 1
                    p.append(''.join(message[i:i + x]))
                    
    return SAPTAKS
def getRagas(phrase):    # main interface
    threshold = 0.6 # threshold at which guesser algorithm starts guessing ragas
    if len(phrase) == 0:
        return 'Your phrase is empty.'
    for note in phrase:
        if note not in 'SrRgGMmPdDnN- ':
            return 'Your phrase has a letter which is not a note. Please reenter your phrase.'
    while '-' in phrase:
        phrase.replace('-', '')
    if len(phrase) < 8:
        return 'Your phrase is too short. Please enter a longer phrase.'
    SAPTAKS = getRagaCount(phrase)
    high = 0
    guesses = []
    for freq in list(SAPTAKS.values()):
        if freq > high:
            high = freq
    keys = list(SAPTAKS.keys())

    for i in keys:
        guess = i
        accuracy = SAPTAKS[guess] / tri(len(phrase))
        
        if accuracy >= threshold:
            guesses.append(guess[:guess.index(':')])
    guesses = ' or '.join(guesses)
    if guesses:
        return 'I think your phrase is a ' + guesses + ' phrase.'
    else:
        return 'I\'m not sure which raga your phrase is in.'
def main():
    while True:
        phrs = input('Enter a phrase and I will guess what raga it is in! > ')
        print(getRagas(phrs))
if __name__ == '__main__':
    main()