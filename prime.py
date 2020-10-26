num = input("Until what number do you want to find prime? \n")
tot = []
for x in range(int(num)):
    i = 0
    for y in range(2, x):
        if x % y == 0:
            pass
        else:
            i = i + 1
    if i == x - 2:
        print(x)
        tot.append(x)
print(len(tot))