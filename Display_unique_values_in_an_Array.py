from collections import Counter

n = input()

a = list(map(int, input().split()))

count = Counter(a)
unique = False

for num in a:
    if count[num] == 1:
        print(num, end=" ")
        unique = True
    
if unique == False:
    print(-1)