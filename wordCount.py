import re

val = input("Enter The File Name: ")
count = 0


readFile = open(val, "r")  # read mode

wordDict = dict()


def populate(name, occurrence):
    name = name.casefold()
    wordDict.update({name: occurrence})


def isPresent(name):
    if name in wordDict.keys():
        return True


for word in readFile.read().split():  # for each word in the file, split
    word = re.sub(r'[^\w\s]', '', word)  # sub punctuations with empty string

    if isPresent(word):  # if the word is there, dont add it, just add to value
        repeated = wordDict.get(word)
        repeated += 1
        wordDict[word] = repeated #set new value

    else:
        populate(word, 1)  # add the word

newFile = open("newFile.txt", "w+")  # over-ride whats on the file

for key, values in sorted(wordDict.items()):  # sort dictionary
    newFile.write(key + ": " + str(values) + "\n")
