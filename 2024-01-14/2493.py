import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())

stack = []

arr = list(map(int, input().split()))
ans = []
count = 0
for i in arr:
    if not stack:
        ans.append(0)
        stack.append([count,i])
        count += 1
    else:
        while stack:
            if stack[-1][1] < i:
                stack.pop()
            else:
                ans.append(stack[-1][0] + 1)
                stack.append([count,i])
                count += 1
                break
        else:
            ans.append(0)
            stack.append([count,i])
            count += 1
for x in ans:
    print(x, end=' ')