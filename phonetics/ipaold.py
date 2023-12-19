'''
assembling the IPA
'''
#import unicodedata
from dataclasses import dataclass

@dataclass
class Manner:
    """
    manner of articulation
    """

    obstruent: bool
    sonorant: bool
    nasal: bool  # = False
    plosive: bool  # = False
    fricative: bool  # = False
    sibilant: bool  # = False
    strident: bool  # = False
    affricate: bool  # = False
    approximant: bool  # = False
    lateral: bool  # = False
    rhotic: bool  # = False
    liquid: bool  # = False
    glide: bool  # = False
    # vibrant = bool = False
    tap: bool  # = False
    trill: bool  # = False

    def isnasal(self):
        """_summary_"""
        self.nasal = True
        self.obstruent = False
        self.sonorant = True

    def isstop(self):
        """_summary_"""
        self.plosive = True
        self.obstruent = True
        self.sonorant = False

    def isfricative(self):
        """_summary_"""
        self.fricative = True
        self.obstruent = True
        self.sonorant = False

    def isaffricate(self):
        """_summary_"""
        self.affricate = True
        self.obstruent = True
        self.sonorant = False

    def isapproximant(self):
        """_summary_"""
        self.approximant = True
        self.obstruent = False
        self.sonorant = True

    def issibilant(self):
        """_summary_"""
        self.sibilant = True
        self.strident = True
        self.obstruent = True
        self.sonorant = False

    def isglide(self):  # -> None
        """_summary_"""
        self.approximant = True
        self.glide = True
        self.obstruent = False
        self.sonorant = True

    def islateral(self):
        """_summary_"""
        self.liquid = True
        self.lateral = True
        self.obstruent = False
        self.sonorant = True

    def isrhotic(self):
        """_summary_"""
        self.liquid = True
        self.rhotic = True
        self.obstruent = False
        self.sonorant = True


@dataclass
class Place:
    """
    place of articulation
    """

    labial: bool  # = False
    coronal: bool  # = False
    dorsal: bool  # = False
    laryngeal: bool  # = False
    front: bool  # = False
    back: bool  # = False
    # lingual = bool = False
    dental: bool  # = False
    alveolar: bool  # = False
    palatal: bool  # = False
    velar: bool  # = False
    glottal: bool  # = False
    labiodental: bool  # = False
    retroflex: bool  # = False
    labiovelar: bool  # = False
    bilabial: bool  # = False
    # grave = bool
    # acute = bool

    def isbilab(self):
        """_summary_"""
        self.labial = True
        self.front = True
        self.bilabial = True
        # self.grave = True

    def isdental(self):
        """_summary_"""
        self.dental = True
        self.front = True
        self.coronal = True
        # self.acute = True

    def isalveo(self):
        """_summary_"""
        self.alveolar = True
        self.coronal = True
        self.front = True

    def ispalatal(self):
        """_summary_"""
        self.palatal = True
        self.dorsal = True
        self.back = True

    def isvelar(self):
        """_summary_"""
        self.velar = True
        self.dorsal = True
        self.back = True

    def isglottal(self):
        """_summary_"""
        self.glottal = True
        self.laryngeal = True
        self.back = True

    def isretroflex(self):
        """_summary_"""
        self.retroflex = True
        self.coronal = True
        self.front = True

    def islabiovelar(self):
        """_summary_"""
        self.labial = True
        self.velar = True
        self.dorsal = True
        self.back = True



@dataclass
class Consonant(Manner, Place):
    """
    consonant traits
    """

    place: Place
    manner: Manner
    voice: bool
    length: int


@dataclass
class Height:
    """
    height of vowel
    """

    close: bool
    near_close: bool
    close_mid: bool
    mid: bool
    open_mid: bool
    near_open: bool
    open: bool


@dataclass
class Backness:
    """
    backness of vowel
    """

    front: bool
    near_front: bool
    central: bool
    near_back: bool
    back: bool


@dataclass
class Vowel(Height, Backness):
    """
    vowel traits
    """

    height: Height
    backness: Backness
    round: bool
    length: int

# first day's progress
