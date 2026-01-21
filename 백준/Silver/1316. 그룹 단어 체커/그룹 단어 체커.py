# https://www.acmicpc.net/problem/1316

n=int(input())
count=0

for _ in range(n):
    group=True
    word=input()
    wlist=[]
    if(len(word)==1):
        count+=1
        continue
    for a in range(1,len(word)):
        wlist+=word[a-1]
        if word[a]!=word[a-1]:
            if word[a] in wlist:
                group=False
                break
            else:
                wlist.append(word[a])
    if group==True:
        count+=1
print(count)