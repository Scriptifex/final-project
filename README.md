Final Project CSPB 2237 Natalie Haught

my project changed - it was originally meant to involve string manipulation via regex, but I ended up pivoting. instead I went with nested classes with attached dictionaries.

basically my project is to tag a symbol, as in an IPA symbol, with all the phonetic information required to work with it in a phonemic capacity. here's a couple external links that you can follow to learn more about IPA and what I'm talking about with "phonetic information": 
https://www.internationalphoneticalphabet.org/ipa-sounds/ipa-chart-with-sounds/

https://en.wikipedia.org/wiki/Manner_of_articulation

https://en.wikipedia.org/wiki/Place_of_articulation

this project is written in Python and should be easily runnable in VSC (where it was written) and I expect Jupyter Notebook too. the only modules imported are the dataclass module. all other imports at the top of a file were written by me and are contained within this assignment.
I would suggest running the main.py file and then looking through the code contained in the phonetics folder. placeart.py has the most detailed documentation/explanation because I added commentary to it first. consonant.py, ipaold.py, and ipavowel.py are uncalled and essentially defunct, but I left them in as documentation of my process, so to speak.

the "highest level" files are manner.py, placeart.py, and vowel.py. 

placeart.py contains the data structures used to tag the information contained in a consonant's place of articulation. place of articulation comes from a combination of the active articulator and the passive articulator. the active articulator (such as the lower lip, the tongue, or the larynx) is the part of the mouth that moves in order to make the sound. the passive articulator (such as the upper lip, the teeth, or the palate/roof of the mouth) is the part of the mouth that is moved towards. typically a consonant's place of articulation is only referred to by the passive place of articulation (e.g. 'dental' for a sound where the passive articulator is the upper teeth), but as both places of articulation are relevant information, I felt the data structure should capture both. 

within placeart.py the highest level structures are ActBas and PassBas, both classes that hold the subclasses for the active and passive articulators respectively. using Python's class inheritance system, I was able to effectively create a series of increasingly more specific classes for the place of articulation, passing along the higher-level information from class to class. (see comments in placeart.py for detailing of specifics)

manner.py serves a similar purpose to placeart.py, but it holds the information for manner of articulation. manner of articulation is divided into a couple different categorizations (obstruent/sonorant and occlusive/continuant), and I felt it would be useful to include the information of both categorizations at once. each manner of articulation therefore has two categories that it falls into: obstruent|sonorant and occlusive|continuant. these classes are more... linearly chained together than in placeart.py, following standard phonetic categorization. the comments in manner.py have further details.

vowel.py defines the non-binary features for vowels - height and backness. it also contains methods for converting between integers, strings, and classes for both height and backness. see the main.py file for examples! 

finally, phone.py holds all the methods to implement the classes defined in the previous three files, and ipa.py holds some functions that access and show off the features tagged to a phoneme in the classes. 