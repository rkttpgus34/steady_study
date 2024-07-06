import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

if n < 100:
    print(n)

else:
    count = 0
    for i in range(100,n+1):
        num_list = list(map(int, str(i)))
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            count += 1
    print(count + 99)



