import pickle

def characterOrder(inFile, length):
    # returns a dictionary with words in it
    words = []
    wordsDict = {}

    with open(inFile, "r") as inFile:
        lines = inFile.readlines()
        length += 1
        for i in lines:
            if len(i) <= length:
                i = i.strip()
                a = "".join(sorted(i))
                tup = (a, i)
                words.append(tup)
                print(tup)

    #stick list in an array, match duplicate keys for values
    for line in words:
        if line[0] in wordsDict:
            wordsDict[line[0]].append(line[1])
        else:
            wordsDict[line[0]] = [line[1]]

    print(wordsDict)
    return(wordsDict)


def store(inData, location):
    "Stores in a data type in binary file using pickle library"
    with open(location, "wb") as myFile:
        pickle.dump(inData, myFile)


def txtFileFormat(inFile, outFile):
    "writes key/value pairs of a dictionary to a .txt file for debugging purposes"
    with open(inFile, "rb") as myFile, open(outFile, "w+") as outFile:
        myPulledInDictionary = pickle.load(myFile)
        for i in myPulledInDictionary.keys():
            word = i + str(myPulledInDictionary.get(i)) + "\n"
            outFile.write(word)


# store(characterOrder("words.txt", 9), "mySavedDict.txt")
# txtFileFormat("mySavedDict.txt", "dict.txt")





