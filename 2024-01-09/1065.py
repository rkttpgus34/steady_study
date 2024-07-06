import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

if n < 100:
    print(n)

if n >= 100:
    count = 0
    for i in range(100, n):
        rem1 = n % 10
        n = n // 10
        rem2 = n % 10
        diff = rem1 - rem2
        flag = 0
        while True:
            rem1 = n % 10
            n = n // 10
            rem2 = n % 10
            if diff != rem1 - rem2:
                flag = 1
                break
            if n < 10:
                break
        if flag == 0:
            count += 1
            print(n)
    print(count + 99)