xAxis=int(input("How many rows? "))
yAxis=int(input("How many columns? "))

for r in range(xAxis):
    for c in range(yAxis):
        print("*", end="")
    print()