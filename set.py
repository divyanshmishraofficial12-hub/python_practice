#unordered ,unchangable ,dont allow duplicates

s1={1,2,3,4,4,5}
print(s1)
print(type(s1))
print(len(si))


# accessing

for i in s1:
    print(i)

(s1.discard('dggsgsgd')) # it doesn't show error if the value is not present in a 
print(s1)
(s1.pop())
print(s1)
(s1.remove(2))  #it shows error if the value is not present in a set
print(s1)

s2={1,2,3,7,8,9}

s3=s1.union(s2) # print all items adding both
print(s3)
s4=s1.intersection(s2)  #
print(s4) #print only unique values
s5=s1.symmetric_difference(s2)
print(s5)
