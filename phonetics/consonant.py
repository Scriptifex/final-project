'''
creates classification for consonants
'''
# from typing import Self
import manner
import placeart
import phone
from dataclasses import dataclass

@dataclass
class Consonant(phone.Phone):
    '''
    classifies sound as a consonant
    '''
    consonant: bool = True
    vowel: bool = False
    manner: any
    place: any
    voice: bool
    def __init__(self, symbol, manner, place, voice:bool, length:int):
        self.symbol = symbol
        self.consonant = True
        self.vowel = False
        self.manner = manner
        self.place = place
        self.voice = voice
        self.length = length
    #def MakeConsonant(symbol, manner, place, voice, length):
        #Self.__init__(symbol, manner, place, voice, length)

@dataclass
class Voiced(Consonant):
    '''
    consonant is voiced
    '''
    voice = True
    def __init__(self, symbol, manner, place, length):
        self.symbol = symbol
        self.consonant = True
        self.vowel = False
        self.manner = manner
        self.place = place
        self.voice = True
        self.length = length
    def __str__(self) -> str:
        return "voiced " + self.place.PoA + " " + self.manner.MoA + " consonant"

@dataclass
class Voiceless(Consonant):
    '''
    consonant is voiceless
    '''
    voice = False
    def __init__(self, symbol, manner, place, length):
        self.symbol = symbol
        self.consonant = True
        self.vowel = False
        self.manner = manner
        self.place = place
        self.voice = False
        self.length = length
    def __str__(self) -> str:
        return "voiceless " + self.place.PoA + " " + self.manner.MoA + " consonant"

@dataclass
class Geminate(Consonant):
    '''
    length is two
    '''
    length = 2

#@dataclass
#class BilabialNasal(Consonant):
#    '''
#    bilabial nasal
#    '''
#    manner = manner.Nasal
#    place = placeart.Bilabial

def MakeConsonant(sym, moa, poa, v: bool, l):
    if v == True:
        Voiced.__init__(sym, moa, poa, l)
    if v == False:
        Voiceless.__init__(sym, moa, poa, l)
    
    #Consonant.__init__(sym, moa, poa)
    #pass
    