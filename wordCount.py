import re

val = input("Enter The File Name: ")
count = 0


readFile = open(val, "r")  # read mode

wordDict = dict()


def populate(name, occurrence):
    wordDict.update({name: occurrence})


def isPresent(name):
    if name in wordDict.keys():
        return True


for word in readFile.read().split():  # for each word in the file, split
    word = re.sub(r'[^\w\s]', '', word)  # using function of regular expression library

    if isPresent(word):
         #print(wordDict.get(word))
        repeated = wordDict.get(word)
        repeated += 1
        wordDict[word] = repeated

    else:
        populate(word, 1)


   # print(word.lower())

    # print(count)
for keys, values in sorted(wordDict.items()):
    print(keys +":",values)



newFile = ("newFile.txt", "w+")




