def solution(phone_book):
    phone = set(phone_book)
    for number in phone:
        for i in range(1,len(number)):
            if number[:i] in phone:
                return False
    return True