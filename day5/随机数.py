import random
s = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
t = True
while t:
    a = random.randint(1, 10)
    if a not in s:
        t = False
s[a] = a
print(s)
