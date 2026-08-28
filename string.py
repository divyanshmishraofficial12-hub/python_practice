#   str="hello world..this is a python code..!"

print(len(str.split()))

# print string multiple times
print(str,str,str ,sep='\n')

# using memebership operator
print("is" in str)
print("ddd" not in str)

#indexing and slicing in strings
a="hello world"

print(a[4])  #positive indexing
print(a[-7])  # negaticv indexing

#slicing and reverse string 
#slicing variable[start:end-1:step]


print(a[2:5])
print(a[-1:4:-1])
print(a[-3:3:-1])


#string methods

#   print(dir(a)) string methods


print(a.capitalize())
print(a.casefold())
print(a.lower())
print(a.upper())
print(a.isupper())
print(a.swapcase())
print(a.title())

#  membership operator  

a="he ll o wo rl d"
b='12345'
print(a)
print(a.isalnum(),"print true if it string cantain alphabet and nummric..!")

print(a.isalpha(), "print true if string only cantain alphabet..!")

print(b.isdigit(),"print true if strig csntsin only digit values..!")

print(a.replace('o', '****'))  # it doesnt change the string but make a new one
print(a)

c="  gg  "
print(c.strip(),"remove the space in string")
print(c.lstrip())# from right side 
print(c.rstrip())  # from left side'''

print(a.islower())
print(a.isupper())
print(a.istitle())

print(a.startswith("hello"))

print(a.split(' ',4))

#  join method

a=['a','b','c','d']
print("---- ".join(a))
