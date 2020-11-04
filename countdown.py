import pickle
import random
from itertools import combinations

class lettersRound:
    constonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"

    def __init__(self, inFile):
        with open(inFile, "rb") as myFile:
            self.words = pickle.load(myFile)
    

    def setAnagram(self, anagram):
        self.anagram = anagram.lower()
        return self.anagram


    def generateWord(self, constonantNum, vowelNum):
        i = x = 0
        string = ""

        while i < constonantNum:
            string += self.constonants[random.randint(0, 20)]
            i += 1
        while x < vowelNum:
            string += self.vowels[random.randint(0, 4)]
            x += 1

        l = list(string)
        random.shuffle(l)
        self.anagram = "".join(l)
        return self.anagram
    
    
    def search(self):
        matches = []
        matchesSorted = []
        wordCount = 0
        structures = self.words.keys()

        for i in subString(self.anagram):
            if i in structures:
                formedWords = self.words.get(i)
                wordCount += len(formedWords)
                matches.append(formedWords)

        for i in matches:
            for j in i:
                matchesSorted.append(j)

        matchesSorted = sorted(matchesSorted, key=len, reverse=True)
        return matchesSorted
    

def subString(string):
    # creates all sub strings for the string
    res = [''.join(l) for i in range(len(string)) for l in combinations(string, i + 1)]
    # puts them in alphabetcal order and excludes words less than minimum
    subString = ["".join(sorted(x)) for x in res]
    # gets rid of duplicates by sticking it in a set then back into a list and sorts them
    return sorted(list(dict.fromkeys(subString)))







