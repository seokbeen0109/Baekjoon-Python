# https://www.acmicpc.net/problem/1181

n=int(input())

words=[]

for i in range(n):
    words.append(input())
    
set_words=set(words)
list_words=list(set_words)
list_words.sort()
list_words.sort(key=len)
for word in list_words:
    print(word)
