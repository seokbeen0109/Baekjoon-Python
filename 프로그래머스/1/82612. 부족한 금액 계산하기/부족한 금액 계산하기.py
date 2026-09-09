def solution(price, money, count):
    answer = 0
    price_1=0
    total=0
    for i in range(count):
        price_1+=price
        total+=price_1
    answer=total-money
    if answer>0:
        return answer
    else:
        return 0