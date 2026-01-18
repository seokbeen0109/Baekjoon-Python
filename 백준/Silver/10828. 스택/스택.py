# https://www.acmicpc.net/problem/10828
import sys
n = int(sys.stdin.readline())
stack=[]

for _ in range(n):
    msg=sys.stdin.readline().split()
    if msg[0]=='push':
        stack.append(msg[1])
    elif msg[0]=='pop':
        if len(stack)==0:
            print('-1')
        else:
            print(stack.pop())
    elif msg[0]=='size':
        print(len(stack))
    elif msg[0]=='empty':
        if len(stack)==0:
            print('1')
        else:
            print('0')
    elif msg[0]=='top':
        if len(stack)==0:
            print('-1')
        else:
            print(stack[-1])