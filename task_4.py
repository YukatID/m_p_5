import itertools
count = 0
for p in itertools.product("0123",repeat=4):
    print(''.join(p))
    count = count + 1
print("total", count)
print()
count = 0
for p in itertools.permutations("0123",4):
    print(''.join(str(x) for x in p))
    count = count + 1
print("total permutations:", count)
print()
count = 0
for p in itertools.combinations("0123",3):
    print(''.join(str(x) for x in p))
    count = count + 1
print("total combinations:", count)