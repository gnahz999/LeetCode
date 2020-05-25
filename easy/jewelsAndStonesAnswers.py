# Python Generators
def jas(J, S):
    return (s in J for s in S)

a = jas("aA", "aAAbbbb")
for x in a:
    print(x)
print(sum(a))

# Python Map function
def jas2(J, S):
    return sum(map(J.count, S))

b = jas2("aA", "aAAbbbb")
print(b)

def jas3(J, S):
    setJ = set(J)
    return sum(s in setJ for s in S)

c = jas2("aA", "aAAbbbb")
print(c)