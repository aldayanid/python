stringTuple = ("1", "2", "3", "5", "6", "7", "8", "9", "10")
stringList = list(stringTuple)
print(stringList)
isthisCorrect = input("Input your string: ")
for i in range(0, len(stringList)):
    stringList[i] = int(stringList[i])
print("Integers: ", stringList)