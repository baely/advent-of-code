f=[0]*9;[f:=f[:h]+[f[h]+1]+f[h+1:] for g in open("input.txt").read() if (h:= ord(g) - 48) >= 0];[(f:= f[1:] + f[:1], f.insert(6, f.pop(6) + f[7])) for _ in [0] * 80];print(sum(f))

f=[0]*9
for g in open("input.txt").read().split(","):f[int(g)]+=1
for i in range(80):f[(i+7)%9]+=f[i%9]
print(sum(f))
