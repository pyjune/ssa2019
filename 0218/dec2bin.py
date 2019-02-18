a = 14
for i in range(7, -1, -1):
    if(a&(1<<i) == 0):
        print(0, end='')
    else:
        print(1, end='')
print()

for i in range(7, -1, -1):
    if (a & (1 << i) != 0):
        print(1, end='')
    else:
        print(0, end='')
