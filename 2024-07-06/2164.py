import sys
from collections import deque

sys.stdin = open("input.txt")
input = sys.stdin.readline

que = deque()

N = int(input())

for i in range(1,N+1):
    que.append(i)

while len(que)!=1:
    que.popleft()
    que.append(que.popleft())    
    print(que)

print(que.popleft())