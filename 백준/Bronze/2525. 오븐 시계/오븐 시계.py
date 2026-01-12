# https://www.acmicpc.net/problem/2525

time_now=list(map(int, input().split())) # 현재 시각
need_time=int(input()) # 필요한 시간
a=(need_time+time_now[1])/60
b=(need_time+time_now[1])%60
if need_time+time_now[1]>=60:
    time_now[0]+=a
    print(int(time_now[0])%24,b)
else:
    print(int(time_now[0])%24,b)
    