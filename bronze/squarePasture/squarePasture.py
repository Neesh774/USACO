f = open("square.in", "r")
g = open("square.out", "w")

lines = f.read()
x1 = int(lines.split()[0])
y1 = int(lines.split()[1])
x2 = int(lines.split()[2])
y2 = int(lines.split()[3])

x12 = int(lines.split()[4])
y12 = int(lines.split()[5])
x22 = int(lines.split()[6])
y22 = int(lines.split()[7])

minX1 = min(x1, x12)
minY1  = min(y1, y12)
maxX2 = max(x2, x22)
maxY2 = max(y2, y22)

squareLength = max(maxX2 - minX1, maxY2 - minY1)
squarea = squareLength * squareLength

g.write(str(squarea))
g.close()