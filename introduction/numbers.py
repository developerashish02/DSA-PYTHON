# a = 10
# print(id(a))
# a = a + 1
# print(id(a))
# a = a + 22
# print(id(a))


# its giving the same id because python does optimization for the same numbers
# but this not true for the all the numbers only python do (-5 to 256)
a = 10
b = 10

print(id(a))
print(id(b))


c = 1000
d = 1000

print(id(c))
print(id(d))
