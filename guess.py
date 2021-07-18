import random

n = int(random.random() * 10)
i = int(input("Please enter your number: "))
attempts = 1

while True:
    attempts += 1
    if  attempts == 3:
        print("max number of attempts reached.")
        break

    if i > n:
        print("Enter lesser")
    elif i < n:
        print("Enter higher")
    else:
        print("Bingo")
        break
    i = int(input("Please enter your number: "))

print("The end!")