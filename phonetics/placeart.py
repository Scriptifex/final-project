"""
classes for place of articulation
"""
from dataclasses import dataclass
# each class has a datastring explaining what the class represents
# all classes have a custom __str__ function that returns an actual sentence 

# hierarchy of data structures:
# [parentheses following the name of a class contain the classes that are called 
# inside the class but are not ancestors]
# ActBas
#   > Front
#       > Labial
#       > Coronal
#           > Laminal
#           > Apical
#           > Subapical
#   > Back
#       > Dorsal
#       > Radical
#       > Laryngeal
# PassBas
#   > PLabial
#   > PDental
#   > PDentiAlveolar
#   > PAlveolar
#   > PostAlveolar
#   > PPalatal
#   > PVelar
#   > PUvular
#   > PPharyngeal
#   > PEpiglottal
#   > PGlottal
# Articulation 
#   > PlaceOfArticulation
#       > Bilabial (ActBas > Front > Labial, PassBas > PLabial)
#       > Labiodental (ActBas > Front > Labial, PassBas > PDental)
#       > Linguolabial (ActBas > Front > Coronal > Laminal, PassBas > PLabial)
#       > Interdental (ActBas > Front > Coronal > Laminal, PassBas > PDental)
#       > Dental (ActBas > Front > Coronal > Apical, PassBas > PDental)
#       > DentiAlveolar (ActBas > Front > Coronal > Laminal, PassBas > PDentiAlveolar)
#       > Alveolar (ActBas > Front > Coronal, PassBas > PAlveolar)
#       > LaminalAlveolar (ActBas > Front > Coronal > Laminal, PassBas > PAlveolar)
#       > ApicoAlveolar (ActBas > Front > Coronal > Apical, PassBas > PAlveolar)
#       > PalatoAlveolar (ActBas > Front > Coronal > Laminal, PassBas > PostAlveolar)
#       > ApicalRetroflex (ActBas > Front > Coronal > Apical, PassBas > PostAlveolar)
#       > AlveoloPalatal (ActBas > Back > Dorsal, PassBas > PostAlveolar)
#       > Retroflex (ActBas > Front > Coronal > Subapical, PassBas > PPalatal)
#       > Palatal (ActBas > Back > Dorsal, PassBas > PPalatal)
#       > Velar (ActBas > Back > Dorsal, PassBas > PVelar)
#       > Uvular (ActBas > Back > Dorsal, PassBas > PUvular)
#       > Pharyngeal (ActBas > Back > Radical, PassBas > PPharyngeal)
#       > EpiglottoPharyngeal (ActBas > Back > Laryngeal, PassBas > PPharyngeal)
#       > Epiglottal (ActBas > Back > Laryngeal, PassBas > PEpiglottal)
#       > Glottal (ActBas > Back > Laryngeal, PassBas > PGlottal)
#   > CoArticulated
#       > Labiovelar (Bilabial (ActBas > Front > Labial, PassBas > PLabial), 
#          Velar (ActBas > Back > Dorsal, PassBas > PVelar))

# for more info, see https://en.wikipedia.org/wiki/Place_of_articulation

@dataclass
class ActBas:
    '''basic features for active place of articulation'''
    front: bool #= False
    back: bool #= False
    labial: bool #= False
    coronal: bool #= False
    dorsal: bool #= False
    radical: bool
    laryngeal: bool #= False
    #laminal: bool
    #apical: bool
    #subapical: bool
    d = {"front": False, "back": False, "labial": False, "coronal": False, "laminal": False, 
         "apical": False, "subapical": False, "dorsal": False, "radical": False, "laryngeal": False}

# active places of articulation are split between front and back: 
# after creating the basic class ActBas to hold everything for active articulation, 
# the classes Front and Back are created to sort the places further

@dataclass
class Front(ActBas):
    '''defines act. place of articulation as front'''
    front = True
    back = False
    dorsal = False
    radical = False
    laryngeal = False
    d = {"front": True}
    #d = ActBas.d | nd
    def __str__(self) -> str:
        return "front articulation"

@dataclass
class Back(ActBas):
    '''defines act. place of articulation as back'''
    back = True
    front = False
    labial = False
    coronal = False
    d = {"back": True}
    #d = ActBas.d | nd
    def __str__(self) -> str:
        return "back articulation"

# now that Front and Back have been created, we start creating the classes that represent
# the places of articulation themselves - these will be referenced later after all the passive
# places of articulation are also established

@dataclass
class Labial(Front):
    '''defines act. place of articulation as labial:
    active articulator is lower lip'''
    labial = True
    coronal = False
    nd = {"labial": True}
    d = Front.d | nd
    def __str__(self) -> str:
        return "act. articulation is labial"

@dataclass
class Coronal(Front):
    '''defines act. place of articulation as coronal:
    active articulator is tongue'''
    coronal = True
    labial = False
    laminal: bool
    apical: bool
    subapical: bool
    nd = {"coronal": True}
    d = Front.d | nd
    def __str__(self) -> str:
        return "act. articulation is coronal"

# Coronal is a broad class that covers basically the front half of your tongue. it is split into 
# three more specific classes, but the level of granularity of tongue tip vs the 'blade' of the 
# tongue vs the underside of the tongue is not necessary for all sounds - some, such as /t/ and 
# /d/, are only classified as coronal instead of laminal or apical or so on. but some sounds do 
# require that level of detail - e.g. laminal alveolar and apico-alveolar sounds are distinguished 
# from each other by the laminal vs apical active articulation, as both are formed on the alveolar
# ridge for the passive place of articulation

@dataclass
class Laminal(Coronal):
    '''defines act. place of articulation as laminal:
    active articulator is blade of tongue'''
    laminal = True
    apical = False
    subapical = False
    nd = {"laminal": True}
    d = Coronal.d | nd
    def __str__(self) -> str:
        return "act. articulation is laminal"

@dataclass
class Apical(Coronal):
    '''defines act. place of articulation as apical:
    active articulator is tip of tongue'''
    apical = True
    laminal = False
    subapical = False
    nd = {"apical": True}
    d = Coronal.d | nd
    def __str__(self) -> str:
        return "act. articulation is apical"

@dataclass
class Subapical(Coronal):
    '''defines act. place of articulation as subapical:
    active articulator is underside of tongue'''
    subapical = True
    laminal = False
    apical = False
    nd = {"subapical": True}
    d = Coronal.d | nd
    def __str__(self) -> str:
        return "act. articulation is subapical"

@dataclass
class Dorsal(Back):
    '''defines act. place of articulation as dorsal:
    active articulator is tongue body'''
    dorsal = True
    radical = False
    laryngeal = False
    nd = {"dorsal": True}
    d = Back.d | nd
    def __str__(self) -> str:
        return "act. articulation is dorsal"

@dataclass
class Radical(Back):
    '''defines act. place of articulation as laryngeal:
    active articulator is larynx'''
    radical = True
    laryngeal = False
    dorsal = False
    nd = {"radical": True}
    d = Back.d | nd
    def __str__(self) -> str:
        return "act. articulation is radical"

@dataclass
class Laryngeal(Back):
    '''defines act. place of articulation as laryngeal:
    active articulator is larynx'''
    laryngeal = True
    radical = False
    dorsal = False
    nd = {"laryngeal": True}
    d = Back.d | nd
    def __str__(self) -> str:
        return "act. articulation is laryngeal"

# now we define first the base class PassBas to hold all passive articulation, and then the places
# of passive articulation. unlike active articulation, these don't have subcategories in the same
# way, so they all have PassBas for a parent.

@dataclass
class PassBas:
    '''defines place of passive articulation'''
    plabial: bool = False
    dental: bool = False
    dentialveolar: bool = False
    alveolar: bool = False
    postalveolar: bool = False
    palatal: bool = False
    velar: bool = False
    uvular: bool = False
    pharyngeal: bool = False
    epiglottal: bool = False
    glottal: bool = False
    d = {"plabial": False, "dental": False, "dentialveolar": False, "alveolar": False, 
         "postalveolar": False, "palatal": False, "velar": False, "uvular": False, 
         "pharyngeal": False, "epiglottal": False, "glottal": False}
    #sd = {"dental": False, "dentialveolar": False, "alveolar": False, "postalveolar": False, 
    #      "palatal": False, "velar": False, "uvular": False, "pharyngeal": False, 
    #      "epiglottal": False, "glottal": False}

@dataclass
class PLabial(PassBas):
    '''defines pass. place of articulation as labial:
    passive articulator is upper lip'''
    plabial = True
    d = {"plabial": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is labial"

# any of these passive articulation classes that have a P prefixed onto the word are because the 
# overall place of articulation (active+passive) has the same name as a passive place of articulation
# the overall PoA gets the default name and the passive PoA gets the prefix, as only the overall
# PoA will be called on - these active and passive PoA classes exist only to inform the later overall
# attributes of the full PoA classes 

@dataclass
class PDental(PassBas):
    '''defines pass. place of articulation as dental:
    passive articulator is upper teeth'''
    dental = True
    d = {"dental": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is dental"

@dataclass
class PDentiAlveolar(PassBas):
    '''defines pass. place of articulation as denti-alveolar:
    passive articulator is upper teeth and alveolar ridge'''
    dental = True
    alveolar = True
    dentialveolar = True
    d = {"dental": True, "alveolar": True, "dentialveolar": True}
    #d = PassBas.d | nd
    #d = PassBas.d
    #d["dental"] = True; d["alveolar"] = True; d["dentialveolar"] = True
    def __str__(self) -> str:
        return "pass. articulation is denti-alveolar"

@dataclass
class PAlveolar(PassBas):
    '''defines pass. place of articulation as alveolar:
    passive articulator is alveolar ridge'''
    alveolar = True
    d = {"alveolar": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is alveolar"

@dataclass
class PostAlveolar(PassBas):
    '''defines pass. place of articulation as post-alveolar:
    passive articulator is back of alveolar ridge'''
    postalveolar = True
    d = {"postalveolar": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is post-alveolar"

@dataclass
class PPalatal(PassBas):
    '''defines pass. place of articulation as palatal:
    passive articulator is hard palate'''
    palatal = True
    d = {"palatal": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is palatal"

@dataclass
class PVelar(PassBas):
    '''defines pass. place of articulation as velar:
    passive articulator is soft palate'''
    velar = True
    d = {"velar": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is velar"

@dataclass
class PUvular(PassBas):
    '''defines pass. place of articulation as uvular:
    passive articulator is uvula'''
    uvular = True
    d = {"uvular": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is uvular"

@dataclass
class PPharyngeal(PassBas):
    '''defines pass. place of articulation as pharyngeal:
    passive articulator is pharynx'''
    pharyngeal = True
    d = {"pharyngeal": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is pharyngeal"

@dataclass
class PEpiglottal(PassBas):
    '''defines pass. place of articulation as epiglottal:
    passive articulator is epiglottis'''
    epiglottal = True
    d = {"epiglottal": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is epiglottal"

@dataclass
class PGlottal(PassBas):
    '''defines pass. place of articulation as glottal:
    passive articulator is glottis'''
    glottal = True
    d = {"glottal": True}
    #d = PassBas.d | nd
    def __str__(self) -> str:
        return "pass. articulation is glottal"

# here's another base class: exists to hold PlaceOfArticulation and CoArticulated together

@dataclass
class Articulation():
    '''base class for articulation'''
    PoA: str
    def PlaceName(self):
        return self.PoA
    def __str__(self) -> str:
        return "place of articulation is " + self.PoA

# the base class PlaceOfArticulation holds all PoA that are called to define a phone(aka sound).
# the only exception is Labiovelar, which is a coarticulated sound. more on that later. 

@dataclass
class PlaceOfArticulation(Articulation):
    '''base class for place of articulation'''
    active: type
    passive: type
    #ad = active.d
    #pd = passive.d
    bilabial: bool = False
    labiodental: bool = False
    linguolabial: bool = False
    interdental: bool = False
    laminalalveolar: bool = False
    apicoalveolar: bool = False
    palatoalveolar: bool = False
    apicalretroflex: bool = False
    alveolopalatal: bool = False
    retroflex: bool = False
    epiglottopharyngeal: bool = False
    d = {"bilabial": False, "labiodental": False, "linguolabial": False, "interdental": False, 
         "laminal alveolar": False, "apico-alveolar": False, "palato-alveolar": False, 
         "apical retroflex": False,"alveolo-palatal": False, "retroflex": False, "epiglotto-pharyngeal": False}
    #del d["plabial"]
    #fd = ad | pd | d#| nd

@dataclass
class Bilabial(PlaceOfArticulation):
    '''place of articulation is bilabial:
    act. articulator is lower lip and pass. articulator is upper lip'''
    active = Labial
    passive = PLabial
    bilabial = True
    PoA = "bilabial"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Labiodental(PlaceOfArticulation):
    '''place of articulation is labiodental:
    act. articulator is lower lip and pass. articulator is upper teeth'''
    active = Labial
    passive = PDental
    labiodental = True
    PoA = "labiodental"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Linguolabial(PlaceOfArticulation):
    '''place of articulation is linguolabial:
    act. articulator is tongue blade and pass. articulator is upper lip'''
    active = Laminal
    passive = PLabial
    linguolabial = True
    PoA = "linguolabial"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Interdental(PlaceOfArticulation):
    '''place of articulation is interdental:
    act. articulator is tongue blade and pass. articulator is upper teeth'''
    active = Laminal
    passive = PDental
    interdental = True
    PoA = "interdental"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Dental(PlaceOfArticulation):
    '''place of articulation is dental:
    act. articulator is tongue tip and pass. articulator is upper teeth'''
    active = Apical
    passive = PDental
    dental = True
    PoA = "dental"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class DentiAlveolar(PlaceOfArticulation):
    '''place of articulation is denti-alveolar:
    act. articulator is tongue blade and pass. articulator is upper teeth/alveolar ridge'''
    active = Laminal
    passive = PDentiAlveolar
    dentialveolar = True
    PoA = "denti-alveolar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Alveolar(PlaceOfArticulation):
    '''place of articulation is alveolar:
    act. articulator is tongue and pass. articulator is alveolar ridge'''
    active = Coronal
    passive = PAlveolar
    alveolar = True
    PoA = "alveolar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class LaminalAlveolar(PlaceOfArticulation):
    '''place of articulation is laminal alveolar:
    act. articulator is tongue blade and pass. articulator is alveolar ridge'''
    active = Laminal
    passive = PAlveolar
    laminalalveolar = True
    PoA = "laminal alveolar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class ApicoAlveolar(PlaceOfArticulation):
    '''place of articulation is apico-alveolar:
    act. articulator is tongue tip and pass. articulator is alveolar ridge'''
    active = Apical
    passive = PAlveolar
    apicoalveolar = True
    PoA = "apico-alveolar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class PalatoAlveolar(PlaceOfArticulation):
    '''place of articulation is palato-alveolar:
    act. articulator is tongue blade and pass. articulator is back of alveolar ridge'''
    active = Laminal
    passive = PostAlveolar
    palatoalveolar = True
    PoA = "palato-alveolar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class ApicalRetroflex(PlaceOfArticulation):
    '''place of articulation is apical retroflex:
    act. articulator is tongue tip and pass. articulator is back of alveolar ridge'''
    active = Apical
    passive = PostAlveolar
    apicalretroflex = True
    PoA = "apical retroflex"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class AlveoloPalatal(PlaceOfArticulation):
    '''place of articulation is alveolo-palatal:
    act. articulator is tongue body and pass. articulator is back of alveolar ridge'''
    active = Dorsal
    passive = PostAlveolar
    alveolopalatal = True
    PoA = "alveolo-palatal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Retroflex(PlaceOfArticulation):
    '''place of articulation is retroflex:
    act. articulator is underside of tongue and pass. articulator is hard palate'''
    active = Subapical
    passive = PPalatal
    retroflex = True
    PoA = "retroflex"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Palatal(PlaceOfArticulation):
    '''place of articulation is palatal:
    act. articulator is tongue body and pass. articulator is hard palate'''
    active = Dorsal
    passive = PPalatal
    palatal = True
    PoA = "palatal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Velar(PlaceOfArticulation):
    '''place of articulation is velar:
    act. articulator is tongue body and pass. articulator is soft palate'''
    active = Dorsal
    passive = PVelar
    velar = True
    PoA = "velar"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Uvular(PlaceOfArticulation):
    '''place of articulation is uvular:
    act. articulator is tongue body and pass. articulator is uvular'''
    active = Dorsal
    passive = PUvular
    uvular = True
    PoA = "uvular"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Pharyngeal(PlaceOfArticulation):
    '''place of articulation is pharyngeal:
    act. articulator is tongue root and pass. articulator is pharynx'''
    active = Radical
    passive = PPharyngeal
    pharyngeal = True
    PoA = "pharyngeal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class EpiglottoPharyngeal(PlaceOfArticulation):
    '''place of articulation is epiglotto-pharyngeal:
    act. articulator is larynx and pass. articulator is pharynx'''
    active = Laryngeal
    passive = PPharyngeal
    epiglottopharyngeal = True
    PoA = "epiglotto-pharyngeal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Epiglottal(PlaceOfArticulation):
    '''place of articulation is epiglottal:
    act. articulator is larynx and pass. articulator is epiglottis'''
    active = Laryngeal
    passive = PEpiglottal
    epiglottal = True
    PoA = "epiglottal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class Glottal(PlaceOfArticulation):
    '''place of articulation is glottal:
    act. articulator is larynx and pass. articulator is glottis'''
    active = Laryngeal
    passive = PGlottal
    glottal = True
    PoA = "glottal"
    nd = {PoA: True}
    ad = ActBas.d|active.d
    pd = PassBas.d|passive.d
    d = ad|pd|PlaceOfArticulation.d | nd 
    #fd = d|ad|pd

@dataclass
class CoArticulated(Articulation):
    '''defines a consonant as co-articulated'''
    primary: type
    prd = dict
    secondary: type
    sd = dict
    d = prd | sd
    PoA: str
    def Labialization(self, prime):
        self.primary = prime
        self.secondary = Labial
        self.prd = prime.d
        self.sd = Labial.d
        if prime == Velar:
            self.PoA = "labiovelar"
            self.nd = {self.PoA: True}
            self.d = self.d | self.nd
        if prime == Dental:
            self.PoA = "labiodental"
            self.nd = {self.PoA: True}
            self.d = self.d | self.nd
        else:
            self.PoA = "labialized " + prime.PoA
            #self.nd = {self.PoA: True}
            #self.d = self.d | self.nd
        return
    def Palatalization(self, prime):
        self.primary = prime
        self.secondary = Palatal
        self.prd = prime.d
        self.sd = Palatal.d
        self.PoA = "palatalized " + prime.PoA
        return
    def Velarization(self, prime):
        self.primary = prime
        self.secondary = Velar
        self.prd = prime.d
        self.sd = Velar.d
        self.PoA = "velarized " + prime.PoA
        return
    def Pharyngealization(self, prime):
        self.primary = prime
        self.secondary = Pharyngeal
        self.prd = prime.d
        self.sd = Pharyngeal.d
        self.PoA = "pharyngealized " + prime.PoA
        return

# some sounds, such as /w/, are actually articulated in two places. a labiovelar is shaped first 
# in the back of the mouth (velar) and additionally with the two lips (bilabial). if I were to 
# spend longer on this project and expand it, I would come here first and fully define all 
# possibilities for coarticulation in a way that you can call and run. as it is, the CoArticulated
# class exists more as a sort of proof of concept.  

#@dataclass
class Labiovelar(CoArticulated, Velar, Bilabial):
    '''defines a consonant as labiovelar'''
    primary: Velar
    prd = Velar.d
    secondary: Bilabial
    sd = Bilabial.d
    PoA = "labiovelar"
    nd = {PoA: True, "bilabial": True, "labial": True, "front": True, "plabial": True}
    d = sd|prd|nd

# these two following functions are very simple - given a full PoA class, they return the 
# dictionaries for the active and passive articulation of a phone.

def GetActDict(obj):
    hold = obj.ad
    return hold

def GetPassDict(obj):
    hold = obj.pd
    return hold
