a = 123456.0
b = str(int(a))
print(b.isdecimal())

# c = 123456
# print(len(c))

print(1.0 == 1)

s = '-100'
print(s.isdecimal())

tup = (('1', 2), ('123', 1,))
lis = list(tup)
for i in range(len(lis)):
    lis[i] = list(lis[i])
print(lis)
