def fb(no):
    a,b=0,1

    while a< no:
        yield 1
        a,b=b,a+b

x= fb(5)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))

