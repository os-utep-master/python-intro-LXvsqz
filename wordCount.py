
val = input("Enter The File Name: ")

#print(val)

readFile = open(val)  # mode r is for reading
for word in readFile.read().split(",", "."):

    print(word)

newFile = ("newFile.txt", "w+")



