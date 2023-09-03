import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

A.sort()

def binary_search(start,end,target,arr):
    while (start<=end):
        mid = (end + start) // 2

        if arr[mid] == target:
            return 1
        
        elif arr[mid] > target:
            end = mid - 1
        
        else:
            start = mid + 1
        
    return 0

for i in B:
    print(binary_search(0, N-1, i, A))