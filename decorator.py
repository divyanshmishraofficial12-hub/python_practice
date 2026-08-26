#decorators :- wrap one function in another function

'''Isko aise samjho ki agar aapko apne 10 alag-alag functions ke aage ya peeche ek hi jaisa kaam (jaise logging karna, user ka permission check karna, ya timing measure karna) jodna ho, toh aapko bar-bar wahi code har function ke andar likhne ki zaroorat nahi padti.'''

def decorator(func):
    def wrapper():
        print("it print BEFORE function..!")
        func()
        print("it print AFTER function..!")
    return wrapper

def hello():
    print("this is my first function")

deco=decorator(hello)
deco() #s tarike mein humein function define karne ke baad ek alag se variable mein usko decorator ke andar pass karna padta hai:


@decorator #  Yeh @ symbol Python mein shortcut (syntactic sugar) ki tarah kaam karta hai. Jaise aapke screenshot mein dikh raha hai:
def sec():
    print("this is a second function..!")

sec()


def dec(fu):
    def nu():
        print("START from here..!")
        fu()
        print("THE GAME ENDS..!")
    return nu
@dec
def game():
    print("thiss is my game..!")

game()


def mk(x):

    def mk1():


        print("Decorated")


        x()


    return mk1


def mk2():

    print("Ordinary")


p = mk(mk2)


p()
