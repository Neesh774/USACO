f = open("breedflip.in", "r")
g = open("breedflip.out", "w")

N = int(f.readline())
A = list(f.readline().strip())
B = list(f.readline())
C = []
for i in range(N):
    C.append(A[i] == B[i])
ans = 0
for i in range(N-2): 
    if C[i] == False and C[i+1] == True:
        ans += 1
g.write(str(ans))
f.close()
g.close()