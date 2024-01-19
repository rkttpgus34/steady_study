import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))
stack = []
ans = [-1 for _ in range(len(seq))]

for x in range(n):
    while stack and (seq[stack[-1]] < seq[x]):
        ans[stack.pop()] = seq[x]
    stack.append(x)


print(*ans)