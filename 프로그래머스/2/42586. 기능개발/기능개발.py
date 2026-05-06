def solution(progresses, speeds):
    answer = []
    while len(progresses)>0:
        count=0
        while len(progresses)>0 and progresses[0]>=100:
            count+=1
            progresses.pop(0)
            speeds.pop(0)
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]
        if count>0:
            answer.append(count)
    return answer