x = int(input())
a = []
for i in range(x):
    a.append([int(i) for i in input().split()])
for i in a:
    print(i[0]%i[1])