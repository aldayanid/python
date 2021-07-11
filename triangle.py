# multiplier = 10
# start = 1
##my version
# while (start <= multiplier):
#     print("*  " * start)
#     start += 1

#rows = int(input("Input rows number: "))
###from right to left
# for y in range(rows):
#     for x in range(rows):
#         print('*' if y+x > rows - 2 else ' ', end='')
#     print()

###from left to right
rows = 10
for y in range(rows):
    for x in range(rows):
        print(" " if y>x else "*", end='')
    print()