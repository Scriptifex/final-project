'''
bringing it all together
'''
import unicodedata
import phonetics.phone
import phonetics.manner
import phonetics.placeart
#import consonant
import phonetics.vowel
from dataclasses import dataclass

def GetManner(obj):
    '''gets the manner of articulation for a consonant'''
    man = obj.manner
    print(man.__str__(man))
    return man

def GetPlace(obj):
    '''gets the place of articulation for a consonant'''
    pla = obj.place
    print(pla.__str__(pla))
    return pla

def GetDict(obj):
    '''gets the dictionary of traits for a phone'''
    hold = obj.d
    print(hold)
    return hold

def GetFeat(obj):
    '''gets the features of a phone by collecting all entries with the value of TRUE'''
    hold = obj.d
    new = {}
    lst = list(hold)
    lst1 = []
    for i in lst:
        if hold[i] == True:
            nd = {i: True}
            lst1.append(i)
            #print(nd)
            new = new|nd
            #print("true")
    #print(new)
    print(lst1)
    return new, lst1         

def HasFeature(obj, f:str):
    '''checks to see if a phone has a given feature'''
    d, lst = GetFeat(obj)
    #lst = []
    for i in lst:
        if i == f:
            print("yes")
            return True
    print("no")
    return False

a = phonetics.phone.CreateVowel("a", "open", "front", False)
e = phonetics.phone.CreateVowel("e", phonetics.vowel.HighMid, phonetics.vowel.Front, False)
i = phonetics.phone.CreateVowel("i", 1, 1, False)
o = phonetics.phone.CreateVowel("o", phonetics.vowel.HighMid, phonetics.vowel.Back, True)
u = phonetics.phone.CreateVowel("u", "high", 5, True)
#y = phonetics.phone.CreateVowel("y", phonetics.vowel.High, phonetics.vowel.Front, True)
#ɪ = phonetics.phone.CreateVowel("ɪ", phonetics.vowel.NearHigh, phonetics.vowel.NearFront, False)
#ʏ = phonetics.phone.CreateVowel("ʏ", phonetics.vowel.NearHigh, phonetics.vowel.NearFront, True)
#ø = phonetics.phone.CreateVowel("ø", phonetics.vowel.HighMid, phonetics.vowel.Front, True)
#ɛ = phonetics.phone.CreateVowel("ɛ", phonetics.vowel.LowMid, phonetics.vowel.Front, False)
#œ = phonetics.phone.CreateVowel("œ", phonetics.vowel.LowMid, phonetics.vowel.Front, False)
#æ = phonetics.phone.CreateVowel("æ", phonetics.vowel.NearLow, phonetics.vowel.Front, False)
#ɶ = phonetics.phone.CreateVowel("ɶ", phonetics.vowel.Low, phonetics.vowel.Front, True)
#ɨ = phonetics.phone.CreateVowel("ɨ", phonetics.vowel.High, phonetics.vowel.Central, False)
#ʉ = phonetics.phone.CreateVowel("ʉ", phonetics.vowel.High, phonetics.vowel.Central, True)
#ɘ = phonetics.phone.CreateVowel("ɘ", phonetics.vowel.HighMid, phonetics.vowel.Central, False)
#ɵ = phonetics.phone.CreateVowel("ɵ", phonetics.vowel.HighMid, phonetics.vowel.Central, True)
#ə = phonetics.phone.CreateVowel("ə", phonetics.vowel.Mid, phonetics.vowel.Central, False)
#ɜ = phonetics.phone.CreateVowel("ɜ", phonetics.vowel.LowMid, phonetics.vowel.Central, False)
#ɞ = phonetics.phone.CreateVowel("ɞ", phonetics.vowel.LowMid, phonetics.vowel.Central, True)
#ɐ = phonetics.phone.CreateVowel("ɐ", phonetics.vowel.NearLow, phonetics.vowel.Central, False)
#ä = phonetics.phone.CreateVowel("ä", phonetics.vowel.Low, phonetics.vowel.Central, False)
#ɯ = phonetics.phone.CreateVowel("ɯ", phonetics.vowel.High, phonetics.vowel.Back, False)
#ʊ = phonetics.phone.CreateVowel("ʊ", phonetics.vowel.NearHigh, phonetics.vowel.NearBack, True)
#ɤ = phonetics.phone.CreateVowel("ɤ", phonetics.vowel.HighMid, phonetics.vowel.Back, False)
#ʌ = phonetics.phone.CreateVowel("ʌ", phonetics.vowel.LowMid, phonetics.vowel.Back, False)
#ɔ = phonetics.phone.CreateVowel("ɔ", phonetics.vowel.LowMid, phonetics.vowel.Back, True)
#ɑ = phonetics.phone.CreateVowel("ɑ", phonetics.vowel.Low, phonetics.vowel.Back, False)
#ɒ = phonetics.phone.CreateVowel("ɒ", phonetics.vowel.Low, phonetics.vowel.Back, True)


#p = phonetics.phone.CreateConsonant("p", phonetics.manner.Plosive, phonetics.placeart.Bilabial, False)
#b = phonetics.phone.CreateConsonant("b", phonetics.manner.Plosive, phonetics.placeart.Bilabial, True)
#m = phonetics.phone.CreateConsonant("m", phonetics.manner.Nasal, phonetics.placeart.Bilabial, True)
#w = phonetics.phone.CreateConsonant("w", phonetics.manner.Semivowel, phonetics.placeart.Labiovelar, True)
#f = phonetics.phone.CreateConsonant("f", phonetics.manner.Fricative, phonetics.placeart.Labiodental, False)
#v = phonetics.phone.CreateConsonant("v", phonetics.manner.Fricative, phonetics.placeart.Labiodental, True)
#n = phonetics.phone.CreateConsonant("n", phonetics.manner.Nasal, phonetics.placeart.Alveolar, True)
#t = phonetics.phone.CreateConsonant("t", phonetics.manner.Plosive, phonetics.placeart.Alveolar, False)
#d = phonetics.phone.CreateConsonant("d", phonetics.manner.Plosive, phonetics.placeart.Alveolar, True)
#ts = phonetics.phone.CreateConsonant("ts", phonetics.manner.SibilantAffricate, phonetics.placeart.Alveolar, False)
#s = phonetics.phone.CreateConsonant("s", phonetics.manner.SibilantFricative, phonetics.placeart.Alveolar, False)
#z = phonetics.phone.CreateConsonant("z", phonetics.manner.SibilantFricative, phonetics.placeart.Alveolar, True)
#ʃ = phonetics.phone.CreateConsonant("ʃ", phonetics.manner.SibilantFricative, phonetics.placeart.PostAlveolar, False)

#GetPlace(w)

