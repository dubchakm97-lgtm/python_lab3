n = int(input())
s = []
for _ in range(n):
    string= input()
    s.append(int(string.split()[0]))
for x in range(100):
    count = 0
    for _ in s:
        if _ <= x:
            count += 1
    print(count, end = ' ')
