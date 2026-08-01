#program to make a calcaulator:-
a=int(input("enter the first nuumber..?"))
b=int(input("enter the second number..?"))
c=(input("enter the function u want to perform..?(+,-,*,//,%)"))

if c == "+":
    print("addition=",a+b)
elif c == "-":
    print("subraction=",a-b)
elif c == "*":
    print("multiply=",a*b)
elif c== "//":
    print("floor devision=",a//b)
elif c== "%":
    print("remainder",a%b)
else:
    print ("error..!not in function");
            
