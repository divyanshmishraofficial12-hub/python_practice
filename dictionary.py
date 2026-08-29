# dictionary is ordered , changable , allow duplicates but not keys consists of key:value pairs

d1={
    'name':'divyansh',
    'age':19,
    'car': ['ford','wagon']
}
print(d1)
print(len(d1))
print(type(d1))

#accesing dictionary

print(d1['name'])
print(d1.get('car'))
print(d1.keys())
print(d1.values())
print(d1.items())

# converting list into dictionary

t1= [('c', 1), ('d', 3)]
ee=dict(t1)
print(type(t1))
print(ee)
print("only print the keys:-",ee.keys())
print(type(ee))

# converting multiple list into dictionary

r=[('d',3),('f',5)]
dd=dict(zip(t1,r))
print(dd)
print(type(dd))

# merging two dict
a={'a': 1, 'b': 2}

b={'c': 3, 'd': 4}

a.update(b)
print(a)
#  dectionary modification and updation

d={
    'name':'divyansh',
    'age':19,
    'car': ['ford','wagon']
}

print(d)
d['name']="shivansh"

print(d)
d.update({'name':"divyansh"})
print(d)

# even add using update

d.update({'course':'BCA'})
print(d)

#  how to remove items from the dictionary

d.pop('age')
print(d)

d.popitem()
print(d)

del d['name']
print(d)

d.clear()

print(d)

# questions

count={}

count[(1,2,3)]=2

count[(4,5,6)]=3

count[(7,8,9)]=4


count[(1,2,3)]=5

print("this is an original dict",count)

add=0
for i in count:
    add=add+count[i]
print(len(count)+add)

# queestion 2

a={i: i*i for i in range (6)}

print(a)

# question 3


student = {
    "name": "Divyansh",
    "roll_no": 1240264048,
    "course": "BCA Cybersecurity",
    "semester": 4
}

for x,y in student.items():
    print(x,y)
    print(f"{x=} and {y=}")
    
