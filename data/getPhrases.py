from guessRaga import NOTES, isValid
import random

f = open('phrases.txt', 'w')
phrasesCreated = 0
while phrasesCreated <= 10000:
    phrase = ''
    phraseLength = random.randint(7, 13)
    for x in range(phraseLength):
        phrase += random.choice(NOTES)
    
    if isValid(phrase):
        f.write('\n' + phrase)
        phrasesCreated += 1
    
f.close()
        
    