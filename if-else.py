'''Task
Given an integer, n, perform the following conditional actions:

If  is odd, print Weird
If  n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 5 to 20, print Weird
If n is even and greater than 20 , print Not Weird'''

number=int(input("enter the number..?"))
 
if number % 2 != 0:
     print("weird")
elif number % 2 == 0 and number >2 and number <5:
    print("not weird")
elif number % 2 == 0 and number >6 and number <20:
    print("more weird")
elif number % 2 == 0 and number > 20:
    print("more and more weird")

#accept the number and print the greatest no between them:-
no1=int(input("enter the no1..?"))
no2=int(input("enter the no2..?"))
 
if no1 > no2:
    print(no1,"is greater")
elif no1 < no2:
    print(no2,"is greater")
else:
    print("error not found..!")

 #accept the gender from user as char andprint some greeting message..
g=input("enter gender in(ex:- M,F)..?")
 
if g == "M" or g =="m":
     print("hello ,good day sir..!")
elif g == "F" or g == "f":
    print("hello ,good day  madam..!")
else:
    print("gender not specific")

#accept integer wheather integer is even or not..?

no=int(input("enter the number..?"))

if no %2 ==0:
    print (f"the {no} is even..!")
else:
    print(f"the {no} is odd..! ")

#accept the name and age from user and check weather he/she is valid voter or not..?
name=input("enter name..?")
age=int(input("enter age in no..?"))

if age <18:
    print(f"{name} , is not eigible to vote..!")
elif age >= 18:
    print(f"{name} , is eligible to vote..!")

#accept a year and check if it  a leap year or not

year=int(input("enter year..?"))

if year % 4 == 0:
    print(f"{year} ,it is a leap year..!")
else:
    print("not a leap year..!")

#take a input from user and ckeck temprature in celcius
 
cel=int(input("enter temprature in celcius..?"))

if cel < 0:
    print(f"{cel} ,freezing cold")

elif cel > 0 or cel <10:
    print(f"{cel}  ,very cold")    
elif cel > 10 or cel <20:
    print(f"{cel} ,very cold") 
else:
    print("not found..!")
        
