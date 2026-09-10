def solution(arr):
    def gcd(a, b):                    # 최대공약수 구하기 (유클리드 호제법)
        while b > 0:
            a, b = b, a % b
        return a
    
    def lcm(a, b):                    # 두 수의 최소공배수
        return a * b // gcd(a, b)
    
    answer = arr[0]
    for num in arr[1:]:
        answer = lcm(answer, num)      # 지금까지의 LCM과 다음 수의 LCM을 계속 구해나감
    
    return answer