'''
vowel features
'''
from dataclasses import dataclass

# vowels have two features that call for classes in my opinion: height and backness. both of these
# attributes can also be treated as scales, and therefore I also represent them with integers in 
# the code. for more information, see here https://en.wikipedia.org/wiki/Vowel

@dataclass
class Height:
    '''height of vowel'''
    height: int
    h: str
    #high: bool
    #near_high: bool
    #mid_high: bool
    #mid: bool
    #mid_low: bool
    #near_low: bool
    #low: bool
    d = {"high": False, "near-high": False, "mid-high": False, "mid": False, "mid-low": False, 
         "near-low": False, "low": False}
    def __str__(self) -> str:
        return "vowel height is " + self.h

@dataclass
class High(Height):
    '''close/high vowel'''
    height = 1
    h = "high"
    #high = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class NearHigh(Height):
    '''near-close/high vowel'''
    height = 2
    h = "near-high"
    #near_high = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class HighMid(Height):
    '''close-mid/mid-high vowel'''
    height = 3
    h = "mid-high"
    #mid_high = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class Mid(Height):
    '''mid vowel'''
    height = 4
    h = "mid"
    #mid = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class LowMid(Height):
    '''open-mid/mid-low vowel'''
    height = 5
    h = "mid-low"
    #mid_low = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class NearLow(Height):
    '''near-open/low vowel'''
    height = 6
    h = "near-low"
    #near_low = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class Low(Height):
    '''open/low vowel'''
    height = 7
    h = "low"
    #low = True
    nd = {h: True}
    d = Height.d | nd

@dataclass
class Backness:
    '''backness of vowel'''
    backness: int
    #front: bool
    #near_front: bool
    #central: bool
    #near_back: bool
    #back: bool
    b: str
    d = {"front": False, "near-front": False, "central": False, "near-back": False, "back": False}
    def __str__(self) -> str:
        return "vowel backness is " + self.b

@dataclass
class Front(Backness):
    '''vowel is front'''
    backness = 1
    b = "front"
    #front = True
    nd = {b: True}
    d = Backness.d | nd

@dataclass
class NearFront(Backness):
    '''vowel is near-front'''
    backness = 2
    b = "near-front"
    #near_front = True
    nd = {b: True}
    d = Backness.d | nd

@dataclass
class Central(Backness):
    '''vowel is central'''
    backness = 3
    b = "central"
    #central = True
    nd = {b: True}
    d = Backness.d | nd

@dataclass
class NearBack(Backness):
    '''vowel is near-back'''
    backness = 4
    b = "near-back"
    #near_back = True
    nd = {b: True}
    d = Backness.d | nd

@dataclass
class Back(Backness):
    '''vowel is back'''
    backness = 5
    b = "back"
    #back = True
    nd = {b: True}
    d = Backness.d | nd

def HeightInt(h):
    if h < 0 or h > 7:
        return "invalid height, enter integer 1-7"
    if h == 1:
        return High
    if h == 2:
        return NearHigh
    if h == 3:
        return HighMid
    if h == 4:
        return Mid
    if h == 5:
        return LowMid
    if h == 6:
        return NearLow
    if h == 7:
        return Low

def HeightConv(high: str):
    '''converts height in string to int'''
    high.strip
    high.lower
    hi = high
    if hi == "close" or hi == "high" or hi == "close/high":
        return 1
    if hi == "near-close" or hi == "nearclose" or hi == "near-high" or hi == "nearhigh" or hi == "near close" or hi == "near high":
        return 2
    if hi == "close-mid" or hi == "closemid" or hi == "midhigh" or hi == "mid-high" or hi == "close mid" or hi == "mid high":
        return 3
    if hi == "mid":
        return 4
    if hi == "open-mid" or hi == "openmid" or hi == "midlow" or hi == "mid-low" or hi == "open mid" or hi == "mid low":
        return 5
    if hi == "near-open" or hi == "nearopen" or hi == "nearlow" or hi == "near-low" or hi == "near open" or hi == "near low":
        return 6
    if hi == "low" or hi == "open" or hi == "open/low":
        return 7
    else:
        return 0

def HeightStr(h):
    high = HeightConv(h)
    hi = HeightInt(high)
    return hi

def BackInt(back):
    if back < 0 or back > 5:
        return "invalid backness, enter integer 1-5"
    if back == 1:
        return Front
    if back == 2:
        return NearFront
    if back == 3:
        return Central
    if back == 4:
        return NearBack
    if back == 5:
        return Back

def BacknessConversion(ba: str):
    '''converts backness in str to int value'''
    ba.strip
    ba.lower
    bac = ba
    if bac == "front":
        return 1
    if bac == "near-front" or bac == "nearfront" or bac == "near front":
        return 2
    if bac == "central":
        return 3
    if bac == "near-back" or bac == "nearback" or bac == "near back":
        return 4
    if bac == "back":
        return 5
    else:
        return 0

def BackStr(back):
    b = BacknessConversion(back)
    ba = BackInt(b)
    return ba

#def 