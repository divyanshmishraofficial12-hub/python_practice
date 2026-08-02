#print for lopp in reverse order
print("the reverse for loop value is:");
for i in range (20,0,-1):
    print(i);
#print value from 0 to number using for loop
for i in range(1,101,1):
  print(i);

#the negative numbering are
    
for i in range (-1,-101,-1):
    print ("the negative numbering from -1 to -101 are:",i);
#the positive reverse order
for i in range (20,1,-1):
    print (i);
#print string by for loop
for i in range(len(a)):
    print(a[i]);
a = "my name is divyansh mishra..wanted to be a pebetration tester"

 #accept a no and print n times hello world 
 
no =int(input("enter the number"))
 
for i in range(no):
     print("hello world")
#print natural no up to n 
no =int(input("enter the number..?"))

for i in range (1,no):
    print(i)  

#revetse for loop print n to 1
n= int(input("enter the no u want to reverse..?")) 

for i in range(n,0,-1):
    print(i);
#print indexin of string
a="nature"
for i in range(len(a)):
    print(i)

#Accept an integer and Print hello world n times
n= int(input("enter the no of terms..?"))

for i in range(1,n):
    print(i,"hello world..!")

#Reverse for loop. Print n to 1
n= int(input("enter the no of terms..?"))

for i in range(n,1,-1):
    print(i)

#Sum up to n terms
n= int(input("enter the no of terms..?"))
sum= 0
for i in range(1,n+1):
    sum+= i
print(sum)
    
# - Print the sum of all even & odd numbers in a range
#separately
n= int(input("enter the no of terms..?"))
sum= 0
if n % 2 == 0:
    for i in range(2,n+1,2):
     sum+= i
    print(sum)

if n % 2!= 0:
    for i in range(1,n+1,2):
        sum+=i
    print(sum)
        
