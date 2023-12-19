'''
classes for manner of articulation
'''
from dataclasses import dataclass

# each class has a datastring explaining what the class represents
# all classes have a custom __str__ function that returns an actual sentence 

# hierarchy of data structures:
# CatBas
#   > ManBas
#       > Obstruent
#       > Sonorant
#       > Occlusive
#       > Continuant
# ManOfArt
#   > Plosive (CatBas > ManBas > Obstruent, CatBas > ManBas > Occlusive)
#   > Nasal (CatBas > ManBas > Sonorant, CatBas > ManBas > Occlusive)
#   > Fricative (CatBas > ManBas > Obstruent, CatBas > ManBas > Continuant)
#   > Affricate (CatBas > ManBas > Obstruent, CatBas > ManBas > Occlusive)
#   > Approximant (CatBas > ManBas > Sonorant, CatBas > ManBas > Continuant)
#       > Semivowel
#   > Liquid (CatBas > ManBas > Sonorant, CatBas > ManBas > Continuant)
#   > Vibrant (CatBas > ManBas > Sonorant, CatBas > ManBas > Continuant)
#       > Tap
#       > Trill
#   > MVowel (CatBas > ManBas > Sonorant, CatBas > ManBas > Continuant)
# SecondArt
#   > Strident
#       > Sibilant
#   > Lateral
#   > Rhotic
#   DualArt (ManOfArt, SecondArt)
#       > SibilantFricative (SecondArt > Strident > Sibilant, Fricative (CatBas > ManBas > 
#          Obstruent, CatBas > ManBas > Continuant))
#       > SibilantAffricate (SecondArt > Strident > Sibilant, Affricate (CatBas > ManBas > 
#          Obstruent, CatBas > ManBas > Occlusive))
#       > LateralFricative
#       > LateralAffricate
#       > LateralApproximant
#       > LateralTap
#       > LateralLiquid
#       > RhoticLiquid

@dataclass
class CatBas():
    '''basic categories for manner of articulation'''
    obstruent: bool
    sonorant: bool
    occlusive: bool
    continuant: bool
    d = {"obstruent": False, "sonorant": False, "occlusive": False, "continuant": False}

# first a base class CatBas is constructed, and then ManBas as a subclass of CatBas. the two are
# split because I felt like it made the data tidier

@dataclass
class ManBas(CatBas):
    '''basic features for manner of articulation'''
    plosive: bool
    nasal: bool
    fricative: bool
    affricate: bool
    approximant: bool
    vibrant: bool
    liquid: bool
    #glide: bool
    #tap: bool
    #trill: bool
    #strident: bool
    #sibilant: bool
    #lateral: bool
    #rhotic: bool
    #d = {"plosive": False, "nasal": False, "fricative": False, "affricate": False, "approximant": False, "glide": False,
    #     "vibrant": False, "tap": False, "trill": False, "liquid": False, "strident": False, "sibilant": False, 
    #     "lateral": False, "rhotic": False}
    #d = CatBas.d | nd

# now we define the four categories. an obstruent cannot be a sonorant (and vice versa). same for
# an occlusive and a continuant. (more on that here https://en.wikipedia.org/wiki/Manner_of_articulation)

@dataclass
class Obstruent(ManBas):
    '''defines manner of articulation as obstruent'''
    obstruent = True
    sonorant = False
    nasal = False
    approximant = False
    liquid = False
    vibrant = False
    d = {"obstruent": True, "sonorant": False}
    #d = ManBas.d | nd

@dataclass
class Sonorant(ManBas):
    '''defines manner of articulation as sonorant'''
    sonorant = True
    obstruent = False
    plosive = False
    fricative = False
    affricate = False
    d = {"sonorant": True, "obstruent": False}
    #d = ManBas.d | nd

@dataclass
class Occlusive(ManBas):
    '''defines manner of articulation as occlusive'''
    occlusive = True
    continuant = False
    fricative = False
    approximant = False
    liquid = False
    vibrant = False
    d = {"occlusive": True, "continuant": False}
    #d = ManBas.d | nd

@dataclass
class Continuant(ManBas):
    '''defines manner of articulation as continuant'''
    occlusive = False
    continuant = True
    plosive = False
    nasal = False
    affricate = False
    d = {"continuant": True, "occlusive": False}
    #d = ManBas.d | nd

# here's the base class for the manners of articulation

@dataclass
class ManofArt():
    '''basic class for manner of articulation'''
    MoA: str
    #d: dict
    d = {"plosive": False, "nasal": False, "fricative": False, "affricate": False, "approximant": False, "glide": False,
         "vibrant": False, "tap": False, "trill": False, "liquid": False, "strident": False, "sibilant": False, 
         "lateral": False, "rhotic": False}
    def MannerName(self):
        return self.MoA
    def __str__(self) -> str:
        return "manner of articulation is " + self.MoA

@dataclass
class Plosive(ManofArt, Obstruent, Occlusive):
    '''manner of articulation is a stop/plosive'''
    plosive = True
    affricate = False
    #strident: bool = False
    #sibilant: bool = False
    MoA = "plosive"
    nd = {MoA: True}
    d = Obstruent.d | Occlusive.d | ManofArt.d | nd

@dataclass
class Nasal(ManofArt, Sonorant, Occlusive):
    '''manner of articulation is a nasal'''
    nasal = True
    MoA = "nasal"
    nd = {MoA: True}
    d = Sonorant.d | Occlusive.d | ManofArt.d | nd

@dataclass
class Fricative(ManofArt, Obstruent, Continuant):
    '''manner of articulation is a fricative'''
    fricative = True
    MoA = "fricative"
    nd = {MoA: True}
    d = Obstruent.d | Continuant.d | ManofArt.d | nd

@dataclass
class Affricate(ManofArt, Obstruent, Occlusive):
    '''manner of articulation is an affricate'''
    affricate: True
    plosive = False
    MoA = "affricate"
    nd = {MoA: True}
    d = Obstruent.d | Occlusive.d | ManofArt.d | nd

@dataclass
class Approximant(ManofArt, Sonorant, Continuant):
    '''manner of articulation is an approximant'''
    approximant = True
    glide: bool
    MoA = "approximant"
    nd = {MoA: True}
    d = Sonorant.d | Continuant.d | ManofArt.d | nd

@dataclass
class Semivowel(Approximant):
    '''manner of articulation is a glide/semivowel'''
    glide = True
    MoA = "glide"
    nd = {MoA: True}
    d = Approximant.d | nd

@dataclass
class Liquid(ManofArt, Sonorant, Continuant):
    '''manner of articulation is a liquid'''
    liquid = True
    #lateral: bool
    #rhotic: bool
    MoA = "liquid"
    nd = {MoA: True}
    d = Sonorant.d | Continuant.d | ManofArt.d | nd

@dataclass
class Vibrant(ManofArt, Sonorant, Continuant):
    '''manner of articulation is vibrant'''
    vibrant = True
    tap: bool
    trill: bool
    MoA = "vibrant"
    nd = {MoA: True}
    d = Sonorant.d | Continuant.d | ManofArt.d | nd

@dataclass
class Tap(Vibrant):
    '''manner of articulation is a tap'''
    tap = True
    trill = False
    MoA = "tap"
    nd = {MoA: True}
    d = Vibrant.d | nd

@dataclass
class Trill(Vibrant):
    '''manner of articulation is a trill'''
    tap = False
    trill = True
    MoA = "trill"
    nd = {MoA: True}
    d = Vibrant.d | nd

@dataclass
class MVowel(ManofArt, Sonorant, Continuant):
    '''manner of articulation is a vowel'''
    mvowel: bool = True
    approximant = False
    vibrant = False
    liquid = False
    MoA = "vowel"
    nd = {MoA: True}
    d = Sonorant.d | Continuant.d | ManofArt.d | nd

# this is a secondary manner of articulation - a primary manner (all above classes) can potentially
# take a secondary manner, depending on the manner. 

@dataclass
class SecondArt():
    '''secondary class for manners of articulation'''
    strident: bool
    sibilant: bool
    lateral: bool
    rhotic: bool
    SMoA: str
    d = {"strident": False, "sibilant": False, "lateral": False, "rhotic": False}
    def MannerName(self):
        return self.SMoA
    def __str__(self) -> str:
        return "secondary manner of articulation is " + self.SMoA

@dataclass
class Strident(SecondArt):
    '''secondary manner of articulation is strident'''
    strident = True
    rhotic = False
    lateral = False
    SMoA = "strident"
    nd = {SMoA: True}
    d = SecondArt.d | nd

@dataclass
class Sibilant(Strident):
    '''secondary manner of articulation is sibilant'''
    sibilant = True
    SMoA = "sibilant"
    nd = {SMoA: True}
    d = Strident.d | nd

@dataclass
class Lateral(SecondArt):
    '''secondary manner of articulation is lateral'''
    lateral = True
    rhotic = False
    sibilant = False
    strident = False
    SMoA = "lateral"
    nd = {SMoA: True}
    d = SecondArt.d | nd

@dataclass
class Rhotic(SecondArt):
    '''secondary manner of articulation is rhotic'''
    lateral = False
    rhotic = True
    sibilant = False
    strident = False
    SMoA = "rhotic"
    nd = {SMoA: True}
    d = SecondArt.d | nd

@dataclass
class DualArt(ManofArt, SecondArt):
    '''dual class for manner of articulation'''
    pass

@dataclass
class SibilantFricative(DualArt, Sibilant, Fricative):
    '''manner of articulation is a sibilant fricative'''
    #sibilant = True
    #strident = True
    MoA = Sibilant.SMoA + " " + Fricative.MoA # "sibilant fricative"
    d = Fricative.d | Sibilant.d

@dataclass
class SibilantAffricate(DualArt, Sibilant, Affricate):
    '''manner of articulation is a sibilant affricate'''
    #sibilant = True
    #strident = True
    MoA = Sibilant.SMoA + " " + Affricate.MoA # "sibilant affricate"
    d = Affricate.d | Sibilant.d

@dataclass
class LateralFricative(DualArt, Lateral, Fricative):
    '''manner of articulation is a lateral fricative'''
    MoA = Lateral.SMoA + " " + Fricative.MoA # "lateral fricative"
    d = Fricative.d | Lateral.d

@dataclass
class LateralAffricate(DualArt, Lateral, Affricate):
    '''manner of articulation is a lateral affricate'''
    MoA = Lateral.SMoA + " " + Affricate.MoA # "lateral affricate"
    d = Affricate.d | Lateral.d

@dataclass
class LateralApproximant(DualArt, Lateral, Approximant):
    '''manner of articulation is a lateral approximant'''
    #glide = False
    MoA = Lateral.SMoA + " " + Approximant.MoA # "lateral approximant"
    d = Approximant.d | Lateral.d

@dataclass
class LateralTap(DualArt, Lateral, Tap):
    '''manner of articulation is a lateral tap'''
    #glide = False
    MoA = Lateral.SMoA + " " + Tap.MoA # "lateral tap"
    d = Tap.d | Lateral.d

@dataclass
class LateralLiquid(DualArt, Lateral, Liquid):
    '''manner of articulation is a lateral liquid'''
    MoA = Lateral.SMoA + " " + Liquid.MoA # "lateral liquid"
    d = Liquid.d | Lateral.d

@dataclass
class RhoticLiquid(DualArt, Rhotic, Liquid):
    '''manner of articulation is a rhotic liquid'''
    MoA = Rhotic.SMoA + " " + Liquid.MoA # "rhotic liquid"
    d = Liquid.d | Rhotic.d
