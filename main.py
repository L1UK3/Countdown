from countdown import lettersRound
from dict_generation import txtFileFormat, store, characterOrder

# store(characterOrder("words.txt", 9), "mySavedDict.txt")
# txtFileFormat("mySavedDict.txt", "dict.txt")

#anagram = input()

word = lettersRound("mySavedDict.txt")
#string = word.setAnagram(anagram)
string = word.generateWord(4,5)
matches = word.search()
length = len(matches[0])
longestWords = 0

for i in matches:
    if len(i) == length:
        longestWords += 1

if longestWords == 1:
    singularPlural = "is"
else:
    singularPlural = "are"

print("\n" + " ".join(string.upper()) + "\n")
print(len(matches), "words have been found")
print("There {} {} {}-letter words\n".format(singularPlural, longestWords, length))
for i in matches:
    if len(i) == length:
        print(i)

print()





