N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

x = 0

for i in range (N):
    if A[i] == B[i]:
        print(i + 1, end=" ")
        x = 1

if x == 0:
    print(0)

