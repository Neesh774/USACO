f = open("word.in", "r")
g = open("word.out", "w")

firstLine = f.readline()
N = int(firstLine.split(" ")[0])
K = int(firstLine.split(" ")[1])

words = f.readline().split(" ")
ans = ""
line = ""
for i in range(N-1):
    ans += words[i]
    line += words[i]
    if len(words[i+1] + line) > K:
        ans += "\n"
        line = ""
    else:
        ans += " "
if len(words[N-1] + line) > K:
    ans += "\n"
ans += words[N-1]
print(ans)
g.write(ans)
g.close()
f.close()