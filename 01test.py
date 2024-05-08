N = int(input())
s = []
for a in range (N):
    s.append(int(input()))

x = 0
y = 0
c = 4

for n in s:
    if c % 4 == 1:
        x -= n
    elif c % 4 == 2:
        y -= n
    elif c % 4 == 3:
        x += n
    else:
        y += n
    c -= 1

print(x,y)
