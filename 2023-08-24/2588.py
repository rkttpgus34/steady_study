import sys

sys.stdin = open("input.txt")

N = int(input())
M = int(input())
sum = 0
for i in range(3):
    sum += (M%10) * N * (10**i)
    print((M%10) * N)
    M = M // 10

print(sum)
