with open('triangles.in') as f:
    next(f)
    points = [tuple(map(int, line.split())) for line in f]

xmin, xmax, ymin, ymax = {}, {}, {}, {}
for x, y in points:
    xmin[y] = min(xmin.get(y, x), x)
    xmax[y] = max(xmax.get(y, x), x)
    ymin[x] = min(ymin.get(x, y), y)
    ymax[x] = max(ymax.get(x, y), y)

result = max(max(x - xmin[y], xmax[y] - x) * max(y - ymin[x], ymax[x] - y)
             for x, y in points)

with open('triangles.out', 'w') as f:
    print(result, file=f)