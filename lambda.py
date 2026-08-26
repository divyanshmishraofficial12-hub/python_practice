#it is a normal function
def add(x):
    return 'answer' ,x + 10

print(add(5))

#lambda function

a= lambda x,y,z: x + y + z
print(a(5,10,15))


#this is a lambda function or ananomyous function

def power(n):
    return lambda a:a**n

square=power(2)  #print square :it holds a:a ** 2
cube=power(3)    #print cube   :it hols a:a ** 3
print("the square is :",square(3))
print("the cube is :",cube(3))



str1="hello"

txt=lambda string: string.upper()[::-1]

print(txt(str1))
