def solution(schedules, timelogs, startday):
    answer = 0
    n=len(schedules)
    for i in range(n):
        hour=schedules[i]//100
        minute=schedules[i]%100
        limit_time=(hour*60)+minute+10
        safe=True
        for day in range(7):
            now=(startday+day-1)%7+1
            if now>=6:
                continue
            real_hour=timelogs[i][day]//100
            real_minute=timelogs[i][day]%100
            real=(real_hour*60)+real_minute
            if real>limit_time:
                safe=False
                break
        if safe:
            answer+=1
    return answer