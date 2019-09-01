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
newFile = open("newFile.txt", "w+")

for key, values in sorted(wordDict.items()):
    newFile.write(key + ":" + str(values) + "\n")


   # print(key + ":" + values)

newFile = open("newFile.txt", "w+")



