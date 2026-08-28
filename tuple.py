#creation and modfication

t1=(21,3,3,4,5,4,5)
print("this is my first tuple:-",t1)
print(type(t1))
print(t1[2])
print(t1[1:4])
print(t1[1:])
print(t1[5:-1])

t=tuple("tuple")
print(t)

# items in tuple are  ordered .immutable , allow duplicates
# question
a=(1,2,3,2,3,4,5)

print(min(a)+max(a)+a.count(2))
