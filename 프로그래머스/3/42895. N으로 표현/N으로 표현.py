def solution(N, number):
    if N==number:
        return 1
    answer=-1
    dp = [set([int(str(N)*(i+1))]) for i in range(8)]
    for i in range(1,8):
        for j in range(i):
            for num1 in dp[j]:
                for num2 in dp[i-j-1]:
                    dp[i].update([num1+num2, num1-num2, num1*num2])
                    if num2!=0:
                        dp[i].add(num1//num2)
        if number in dp[i]:
            answer = i+1
            break
    return answer