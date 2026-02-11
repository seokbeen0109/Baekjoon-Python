# https://www.acmicpc.net/problem/10815
import sys
input=sys.stdin.readline
n=int(input())
n_card=list(map(int, input().split()))
m=int(input())
m_card=list(map(int, input().split()))

n_card.sort()

def binary(start, end, goal, card):
    while start<=end:
        mid=(start+end)//2
        if goal==card[mid]:
            return 1
        elif goal>card[mid]:
            start=mid+1
        else:
            end=mid-1
    return 0
    
for card in m_card:
    print(binary(0,len(n_card)-1, card, n_card),end=" ")