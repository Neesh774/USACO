import sys
f = open("herding.in", "r")
g = open("herding.out", "w")


def checkDone(cows):
    if cows[1] == cows[0] + 1 and cows[2] == cows[0] + 2:
        return True
    return False

cows = f.readline().split(" ")
for i in range(len(cows)):
    cows[i] = int(cows[i])
cows.sort()
min = min(cows[2]-cows[1]-1, cows[1]-cows[0]-1)
max = max(cows[2]-cows[1]-1, cows[1]-cows[0]-1)
print(str(min) + '\n' + str(max))
g.write(str(min) + '\n' + str(max))