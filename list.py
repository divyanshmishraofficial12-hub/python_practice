#ordered changable and allow duplicates

a=[20,33,44,44,4]
print(a)
print(type(a))


#range in list

l1=list(range(11))
print("the list that pribnts:-",l1)

l2=list(range(5,25))
print(l2)

l3=list(range(1,22,2))
print(l3)

#slicing in list..!

li=[12,33,2,44,77,53,55]
print(li)
li[2]="dgsg"
print(li)  #list has changed

print(li[2::2]) #with the help of index
