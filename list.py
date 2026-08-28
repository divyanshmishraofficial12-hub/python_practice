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

# removing items from the list

print(d)
d.remove(33) # removed 33 from this list
print(d)

d.pop(1) # remove item present at index no 1
print(d)

del d[:2]  # help to delete range of itemss
print(d)

d.clear()  # clear the entire list
print(d)

rint(xx.index("my"))  # give index no
print(xx.count("my"))  # count the accurance
xx.reverse()  # reverse the list
print(xx)

xx.sort()  # in ascending or descending order
print(xx)
print(ord('a'))  # gives ACSII value 
xx.sort(key=str.lower)
print(xx)
print(max(xx))


# membership operator in list

gg=[21,33,4,88,66,77]


if 333 in gg:
    print("this is present")
else:
    print("not present")
#nested list

#question
list1=[]
for i in range (3):
    list1. append ([])
    for j in range (3):
        list1 [i]. append (j)
for i in list1:
    print (i)
l3=[[22,33,44],[55,66,77],[88,99,00]]

print(l3)
print(l3[1][2])

# list comprihension

name=['ram','lakhan',"div","sfss"]
start_with_a=[]

for a in name:
    if 'a' in a:
        start_with_a.append(a)
print("it consist of list that starting with a",start_with_a)


# other comprehnsion

dd=[no*2 for no in range(11) if no %2==0]
print(dd)

ss=["hlo","fddsgs","egge"]
gf=[no for no in ss if 'g' in no]
print(gf)
