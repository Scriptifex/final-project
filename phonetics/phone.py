'''
phone class
'''
from dataclasses import dataclass
import phonetics.manner
import phonetics.placeart
import phonetics.vowel

# this file holds the classes and functions to construct vowels and consonants. it pulls together 
# the classes built up in placeart.py, manner.py, and vowel.py. 

@dataclass
class Phone():
    '''
    basic class for a phone
    '''
    symbol: str
    consonant: bool
    vowel: bool
    length: int
    lstr: str

@dataclass
class Consonant(Phone):
    '''classifies sound as a consonant'''
    consonant = True
    vowel = False
    manner: type
    mstr: str
    md: dict # dictionary for manner features
    place: type
    pstr: str
    pd: dict # dictionary for place features
    voice: bool
    vstr: str
    d: dict # dictionary of all features
    def __init__(self, symbol):
        self.symbol = symbol
        self.consonant = True
        self.vowel = False
        self.manner = phonetics.manner.Plosive
        self.place = phonetics.placeart.Front
        self.voice = False
        self.length = 0
        self.lstr = ""
        self.vstr = ""
        self.mstr = ""
        self.pstr = ""
        self.md = {}
        self.pd = {}
        self.d = self.md|self.pd
        return
    def SetPlace(self, place):
        '''set place of articulation'''
        self.place = place
        self.pstr = place.PoA
        self.pd = place.d
        return
    def SetManner(self, manner):
        '''set manner of articulation'''
        self.manner = manner
        self.mstr = manner.MoA
        self.md = manner.d
        return
    def SetVoice(self, voice):
        '''set voiced quality'''
        self.voice = voice
        if voice == True:
            self.vstr = "voiced"
            self.d = self.d|{"voice": True}
        if voice == False:
            self.vstr = "voiceless"
            self.d = self.d|{"voice": False}
        return
    def __str__(self) -> str:
        return self.symbol + ": " + self.lstr + " " + self.vstr + " " + self.pstr + " " + self.mstr

@dataclass
class Vowel(Phone):
    '''classifies sound as a vowel'''
    consonant = False
    vowel = True
    height: type
    hstr: str
    hint: int
    hd: dict
    backness: type
    bstr: str
    bint: int
    bd: dict
    round: bool
    rstr: str
    d: dict
    manner = phonetics.manner.MVowel
    def __init__(self, symbol):
        self.symbol = symbol
        self.consonant = False
        self.vowel = True
        self.height = phonetics.vowel.High
        self.backness = phonetics.vowel.Front
        self.round = False
        self.length = 0
        self.hstr = ""
        self.bstr = ""
        self.lstr = ""
        self.rstr = ""
        self.hint = 0
        self.bint = 0
        self.hd = {}
        self.bd = {}
        self.d = self.hd|self.bd
    def SetHeight(self, hi):
        '''set height of vowel'''
        n = hi
        #print(n)
        if type(hi) == int:
            n = phonetics.vowel.HeightInt(hi)
            #print(n)
            self.height = n
            self.hstr = n.h
            self.hint = n.height
            self.hd = n.d
            return
        if type(hi) == str:
            n = phonetics.vowel.HeightStr(hi)
            self.height = n
            self.hstr = n.h
            self.hint = n.height
            self.hd = n.d
            return
            #n = p
        else: n = hi
        self.height = n
        self.hstr = n.h
        self.hint = n.height
        self.hd = n.d
        return
    def SetBackness(self, ba):
        '''set backness of vowel'''
        n = ba
        if type(ba) == int:
            n = phonetics.vowel.BackInt(ba)
        if type(ba) == str:
            n = phonetics.vowel.BackStr(ba)
        self.backness = n
        self.bstr = n.b
        self.bint = n.backness
        self.bd = n.d
    def SetRound(self, round):
        '''set roundness of vowel'''
        self.round = round
        if round == True:
            self.rstr = "rounded"
            self.d = self.d|{"round": True}
        if round == False:
            self.rstr = "unrounded"
            self.d = self.d|{"round": False}
        return
    def __str__(self) -> str:
        return self.symbol + ": " + self.lstr + " " + self.hstr + " " + self.bstr + " " + self.rstr + " vowel"

def SetLength(l, obj):
    '''set phone length'''
    obj.length = l
    if obj == Vowel:
        if l == 1:
            obj.lstr = "short"
        if l == 2:
            obj.lstr = "long"
        if l == 3:
            obj.lstr = "trimoric"
        if l > 4:
            obj.lstr = "too long??"
        if l < 1:
            obj.lstr = "nonexistent"
        return
    if obj == Consonant:
        if l == 1:
            obj.lstr = ""
        if l == 2:
            obj.lstr = "geminate"
        if l > 3:
            obj.lstr = "I don't think consonants can be that long"
        if l < 0:
            obj.lstr = "nonexistent"
        return

# these two functions serve as an easy single-line call to create consonants and vowels

def CreateVowel(sym:str, h, b, r:bool):
    '''creates a fully featured vowel'''
    v = Vowel(sym)
    v.SetHeight(h)
    v.SetBackness(b)
    v.d = v.hd|v.bd
    v.SetRound(r)
    SetLength(1, v) # default length is 1 - other lengths would appear in the context of a word
    print (str(v))
    return v

def CreateConsonant(sym:str, m, p, v:bool):
    '''creates a fully-featured consonant'''
    c = Consonant(sym)
    c.SetPlace(p)
    c.SetManner(m)
    c.d = c.pd|c.md
    c.SetVoice(v)
    SetLength(1, c)
    print (str(c))
    return c
