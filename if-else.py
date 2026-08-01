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
