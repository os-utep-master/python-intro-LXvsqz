import re

val = input("Enter The File Name: ")
count = 0

readFile = open(val, "r")  # read mode

for word in readFile.read().split():  # for each word in the file, split
    word = re.sub(r'[^\w]', '', word)  # using function of regular expression library
    count += 1
    print(word.lower())
    print(count)

newFile = ("newFile.txt", "w+")



