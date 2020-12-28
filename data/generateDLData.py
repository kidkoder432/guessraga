import multiprocessing
print('Phase 1: Generating data...')
import itertools, random
l = list(itertools.product(list('SRGMPDNrgmdn'), repeat=5))# + list(itertools.product(list('SRGMPDNrgmdn'), repeat=6))
from guessRaga import *
def isValid(phrase):
    for x in range(len(phrase) - 1):
        if phrase[x].lower() == phrase[x+1].lower() and ((phrase[x].islower() and phrase[x+1].isupper()) or (phrase[x].isupper() and phrase[x+1].islower())):
            return False
    return True

def op(phrase):
    gs = None
    if isValid(phrase):
        gs = getRagas(phrase, 0.7)
        
    if gs and len(gs.split(' or ')) == 1:
        return [phrase, gs]
        
def conv(phrase):
    n = NOTES
    o = []
    for p in phrase:
        o.append(str(n.index(p)))
    return ', '.join(o)
if __name__ == '__main__':
    gs = 0
    import time
    t = time.time()
    with multiprocessing.Pool(4) as pool:
        d = pool.map(op, l)

    f = open('dldata.csv', 'w')
    for x in d:
        if x:
            f.write('\n' + conv(x[0]) + ', ' + str(RAGAS.index(x[1])))
    f.close()
    e = time.time()
    print(e-t)