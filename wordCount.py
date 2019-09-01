
val = input("Enter The File Name: ")

#print(val)

readFile = open(val, "r")  # mode r is for reading
for word in readFile.read().split():

    print(word.lower())

newFile = ("newFile.txt", "w+")



