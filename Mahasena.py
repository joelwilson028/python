n = int(input())
a = list(map(int, input().split()))[:n]
count = 0
count1 = 0
for i in a:
    if i % 2 == 0:
        count += 1
    else:
        count1 += 1
if count > count1:
    print("READY FOR BATTLE")
else:
    print("NOT READY")