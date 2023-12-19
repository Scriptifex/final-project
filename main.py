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

#print(phonetics.ipa.GetManner(t))

# there's the manner, how about the place?

#print(phonetics.ipa.GetPlace(t))

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

# for fun, here's everything you can run on these phones:

#phonetics.ipa.GetManner(t)
#phonetics.ipa.GetPlace(t)
#phonetics.ipa.GetDict(t)
#phonetics.ipa.GetFeat(t)
#phonetics.ipa.HasFeature(t, "alveolar")
#phonetics.phone.SetLength(1, t)

# that's about all for demonstrating things to run, but do check out the code itself!

# and if you're interested, here are a bunch of phones that I've already defined! feel free to 
# uncomment them and try running some of the functions listed above on them (I don't believe 
# it'll break anything - I've tested them all)

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

