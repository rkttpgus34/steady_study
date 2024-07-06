import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

n = int(input())
top = list(map(int, input().split()))
stack = []
ans = []
count = 0
for i in top:
    if not stack:
        stack.append([count, i])
        ans.append(0)
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
            stack.append([count,i])
            count += 1
            ans.append(0)

for x in ans:
    print(x, end=' ')

