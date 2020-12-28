from guessRaga import getRagas, tri
def isValid(phrase):
    for x in range(len(phrase) - 1):
        if phrase[x].lower() == phrase[x+1].lower():
            return False
    return True
import random, itertools
print('Welcome To Guess Raga Test!')
print('Follow the prompts. Hit CTRL-C to save and quit.')
phrases = [p for p in itertools.product(list('SRGMPDNrgmdn'), repeat=6)]
nt, npt = [True, True]
f = open('log.csv')
phrasesTested = len(str(f.read()).split('\n')) - 1
nt = 'Phrase, Computer Guesses, User Guesses' not in str(f.read())
npt = 'Phrases tested' not in str(f.read())
print(phrasesTested)
f.close()
f = open('log.csv', 'a')
if nt:
    f.write('Phrase, Computer Guesses, User Guesses')
correct = 0
threshold = 0.3
try:
    while phrasesTested < 1000:
        phrase=list(random.choice(phrases))
        if not isValid(phrase):
            phrase = []
            continue
        print('Phrase # %s: %s' %(phrasesTested + 1, ''.join(phrase)))
        # guesses = getRagas(phrase)
        if guesses:
            print('I think your phrase is a ' + guesses + ' phrase.')
            userGuesses = input('Which ragas is it really in? Enter your guesses seperated by "&" > ')
            for g in userGuesses.split('&'):
                if g in guesses:
                    correct += 1
                    break

        else:
            guesses = ['Not Sure']
            print('I\'m not sure which raga your phrase is in.')
            userGuesses = input('Which ragas is it really in? Enter your guesses separated by "&". Or enter a blank if you\'re not sure either. > ')
        f.write('\n')
        if userGuesses == '':
            userGuesses = 'Not Sure'
        f.write(''.join(phrase) + ', ' + '/'.join(guesses) + ', ' + '/'.join(userGuesses.split('&')))
        phrasesTested += 1
        phrase = []
except KeyboardInterrupt:
    print('\nSaving progress...')
    f.close()
