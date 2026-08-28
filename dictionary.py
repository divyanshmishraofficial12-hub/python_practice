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
