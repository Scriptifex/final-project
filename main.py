import phonetics.ipa
import phonetics.phone
import phonetics.vowel
import phonetics.manner
import phonetics.placeart

# for this little main file, I suggest un-commenting out the lines of code in sequence as you read
# along. if uncommented all at once, you'll get your terminal flooded

# let's take the consonant /t/, which is defined as a voiceless alveolar plosive
# and add that information to a variable called t
t = phonetics.phone.CreateConsonant("t", phonetics.manner.Plosive, phonetics.placeart.Alveolar, False)
# the function CreateConsonant also prints out the phonetic features in the terminal
# check out the corresponding wikipedia page! https://en.wikipedia.org/wiki/Voiceless_dental_and_alveolar_plosives
# now let's create the same sound, but this time voiced!
d = phonetics.phone.CreateConsonant("d", phonetics.manner.Plosive, phonetics.placeart.Alveolar, True)
# wow, /t/ and /d/ are a minimal pair! they're only distinguished by one feature (voicing)
# https://en.wikipedia.org/wiki/Voiced_dental_and_alveolar_plosives here's the page for /d/
# now let's inspect these consonants a bit. see what we can get from them

print(phonetics.ipa.GetManner(t))

# there's the manner, how about the place?

print(phonetics.ipa.GetPlace(t))

# part of setting up all these classes was also setting up dictionaries to hold all the features.
# let's grab the dictionary for /t/ and see what exactly is being contained in there

#phonetics.ipa.GetDict(t)

# that's a lot of data and most of it is False. (but as you can see, the state of every possible
# feature gets collected and passed along through the classes until we create The Consonant.) but
# since it's so much data, it would be nice to just see everything that's true about the phone

#phonetics.ipa.GetFeat(t)

# GetFeat returns a dictionary containing only the True keys from the full dictionary, as well as 
# a list with just the keys. 
# we can see that /t/ is a front coronal alveolar plosive, meaning it's therefore an obstruent and
# an occlusive as well. 

#phonetics.ipa.GetFeat(d)

# we can also check if a phone has a given feature
#phonetics.ipa.HasFeature(d, "voice")
#phonetics.ipa.HasFeature(t, "voice")

# now for vowels...

#a = phonetics.phone.CreateVowel("a", "open", "front", False)
#e = phonetics.phone.CreateVowel("e", phonetics.vowel.HighMid, phonetics.vowel.Front, False)
#i = phonetics.phone.CreateVowel("i", 1, 1, False)
#o = phonetics.phone.CreateVowel("o", phonetics.vowel.HighMid, phonetics.vowel.Back, True)
#u = phonetics.phone.CreateVowel("u", "high", 5, True)

# you can see that the CreateVowel function has been set up to take varying forms of input for
# height and backness. (see the code in vowel.py for the details). just thought this would be fun.

# that's about all for demonstrating things to run, but do check out the code itself!
