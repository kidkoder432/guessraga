RAGAS = '''Abhogi: SRgMDS SDMgRS
Adana: SRMPdnS SdnPgMRS
Ahir Bhairav: SrGMPDnS SnDPMGMGrS
Amritvarshini: SGmPNS SNPmGS
Bageshree: SgMDnS SnDMPDMgRS
Bageshrikauns: SgMDnS SnDMgS
Bahaar: SMPnDNS SnPgMRS
Bairagi: SrMPnS SnPMMrS
Barawa: SRMPDnDS SnDPgRMGPMgRS
Basant: SMGmdNS SNdPmGmGrS
Bhairav: SrGMPdNS SNdPMGMGrS
Bhairavi: SgMdnSRgrS SndPMPgMrS
Bhatiyar: SrGMmDNS rNDPMGPGrS
Bhimpalasi: nSgMPnS SnDPMPgRS
Bhinna Shadja: SGMDNS SNDMGS
Bhoopali: SRGPDS SDPGRS 
Bhoopali Todi: SrgPdS SdPgrS
Bibhas: SrGPdS SdPGrS
Bihag: SGMPNS SNDPmPGMGRS
Bihagda: SGMPNS SNDPDnDPGMGRS
Bilaskhani Todi: SrgPdS rndMgrS
Bilawal: SGRGPDNS SNDnDPMGRS
Vrindavani Sarang: SRMPNS SnPMRS
Chandrakauns: SgMdNS SNdMgS
Charukeshi: SRGMPdnS SndPMGRS
Chhayanat: SRGMPmPDNS SNDnDPPmDPmPMGRS
Darbari Kanada: SRMgMPdnS SndnPgMRS
Des: SRMPNS SnDMPDMGRGS
Dhani: SgMPnS SnPMgS
Durga: SRMPDS SDPMRS
Gorakh Kalyan: SRMDnS SnDMRMPMRS
Gaud Malhar: SMRPMPnDNS SnPGPDPMGRS
Gujari Todi: SrgmdNS SNdmgrS
Gunakali: SrMPdS SdPMrS
Hameer: SGMNDNS SNDPmPGMRS
Hansadhwani: SRGPNS SNPGRS
Hindol: SGmDNS SNDmGS
Janasammohini: SRGPDnS SnDPGRS
Jaijaivanti: SRGMPNS SnDPMGRgRS
Jait: SrGPDS SDPGrS
Jog: SGMPnS SnPMGgS
Jogkauns: SGMdNS SNdndPMGgS
Jogiya: SrMPdS SNdPMGrS
Jaunpuri: SRMPdnS SndPdMPgRS
Kafi: SRMPDnDS SnDPMgRS
Kalavati: SGPDnS SnDPGS
Kalingada: SrGMPdNS SNdPMGrS
Kamod: SRmPDPNS SDPGMRS
Kedar: SMGPmPNS SNDPmPDPMRS
Kirvani: SRgMPdNS SNdPMgRS
Khamaj: SGMPDnS SnDPMGRS
Kolahas: SRgPDnS SnDPgRS
Lalat: NrGMmMdNS SNdmdmMGrS
Madmaad Sarang: SRMPnS SnPMRS
Madhukauns: SgmPnS SnPmgS
Madhuvanti: SgmPNS SNDPmgRS
Malkauns: SgMdnS SndMgS
Malhar: SMRPnDNS SnPgMRS
Mand: SGMPDNS SNDPMGRS
Marwa: rGmDNrS rNDmGrS
Marubihag: SMGmPNS SNDPmGRS
Multani: SgmPNS SNdPmgrS
Nand: SGMPDNPS SNDPMGMDPMRS
Nat Bhairav: SGMPdNS SNdPMGMGRS
Nayaki Kanada: SRMPnS SnPgMRS
Paraj: SGmdNdS SNdNdPmGMGrS
Parameshwari: SrgMDnS SnDMgrS
Patadeep: SgMPNS SNDPMgRS
Pooriya: NrGmDNrS rSNDmGmrGrS
Pooriya Kalyan: NrGmDNS SNDPmGrS
Pooriya Dhanashree: NrGmdNS rNdPmGrS
Poorvi: NrGmdNS SNdPmGMGrS
Rageshri: SGMDnS SnDMGRS
Rajakalyan: NRGmDNS SNDmGRS
Ramadasimalhar: SRGMPnDNS SnPgMRS
Ramakali: SGMdNS SNdPmPdndPGMGrS
Salag Varali: SrgPDnS SnDPgrS
Saraswati: SRmPDS SnDPmRS
Shahanakanada: SRgMPgMDnS SnPgMRS
Shankara: SGPNDS SNPGPRGRS
Shivaranjani: SRgPDS SDPgRS
Shree: SrmPNS rNdPdmGrS
Shuddha Kalyan: SRGPDS SNDPmGRS
Shuddha Sarang: SRmPNS SNDPMRS
Shyam Kalyan: SRmPNS SNDPmPGMRS
Sohani: SGmDNSrS SNDmGrS
Soora Malhar: SRMPDnDMPNS SnDPMRS
Sorath: SRMPNS SnDPDMRS
Tilakakamod: SRMPNS SPDMGSRGS
Tilanga: SGMPNS SnPGMGRS
Todi: SrgmdNS SNdPmgrS
Yaman: NRGmDNS SNDPmGRS
Yaman Kalyan: NRGmDNS SNDPmGMGRS
Jinjhoti: SRMPDnDS SnDMGSMRS'''.split('\n')
def tri(n): #triangular number calculator
    t = 0
    for i in range(n):
        t += i
    return t
def validate(phrase):
    if len(phrase) == 0:
        guesses =  'Your phrase is empty.'
    for note in phrase:
        if note not in 'SrRgGMmPdDnN- ':
            guesses =  'Your phrase has a letter which is not a note. Please reenter your phrase.'
    while '-' in phrase:
       phrase = phrase.replace('-', '')
    if len(phrase) < 5:
        guesses = 'Your phrase is too short. Please enter a longer phrase.'
    else:
        guesses = getRagas(phrase)
    
def loadDictionary(): # open raga database
#    dictionaryFile = open("raga-index.txt")
    englishWords = {}
    for word in RAGAS:
        englishWords[word] = 0
#    dictionaryFile.close()
    return englishWords    
def getRagas(phrase, threshold=0.5, joiner=' or '): # guessing code

    SAPTAKS = loadDictionary()
    for x in range(2, 4):
        for i in range(len(phrase) - x + 1):
            for saptak in list(SAPTAKS.keys()):
                if ''.join(phrase[i:i + x]) in saptak[saptak.index(': '):]:
                    print(''.join(phrase[i:i + x]), saptak[:saptak.index(': ')])
                    SAPTAKS[saptak] += 1
    guesses = []           
    keys = list(SAPTAKS.keys())
    for i in keys:
        guess = i
        if SAPTAKS[guess] / tri(len(phrase)) >= threshold:
            guesses.append(guess[:guess.index(':')])
    guesses = joiner.join(guesses)
    if not guesses:
        guesses = 'I\'m not sure which raga your phrase is in.'        
    return guesses

def main():   # main interface
    SAPTAKS = loadDictionary()
    phrase = input('Enter a phrase and I will guess what raga it is in! > ')  
    threshold = 0.7 # threshold at which guesser algorithm starts guessing ragas
    if len(phrase) == 0:
        return 'Your phrase is empty.'
    for note in phrase:
        if note not in 'SrRgGMmPdDnN- ':
            return 'Your phrase has a letter which is not a note. Please reenter your phrase.'
    while '-' in phrase:
        phrase.replace('-', '')
    if len(phrase) < 5:
        return 'Your phrase is too short. Please enter a longer phrase.'
    guesses = getRagas(SAPTAKS, phrase, threshold, '/')
    if guesses:
        print('I think your phrase is a ' + guesses + ' phrase.')
    else:
        print('I\'m not sure which raga your phrase is in.')

if __name__ == '__main__':
    while True:
        main()