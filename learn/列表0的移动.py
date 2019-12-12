ls=eval(input())
i=0
while 0 in ls:
    s=ls.index(0)
    del ls[s]
    i=i+1
for x in range(i):
    ls.append(0)
print(ls)
