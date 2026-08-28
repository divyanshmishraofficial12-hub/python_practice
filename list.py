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

#  print(dir(list))   gives the directory of the list 

d=[21,33,44,55,55]
print("this is my list:-",d[1:3])

d[1]="apple"

print("this is my changed list:-",d)

d[2:4]="banana","mango"

print("changing multiple items:-",d)


# modification of list
print(d)
d.append("onge") #join at the last of list

print(d)

d.insert(2,"flu flu")  # join at desired index position 
print(d)

# adding item to a list
f=[88,77,66]

h=d+f  # adding normaly concate
print(h)
print(d)
j=["hhdh","grr"]
d.extend(j) # use to add collection of items(list,tuple,set)

print(d) 
