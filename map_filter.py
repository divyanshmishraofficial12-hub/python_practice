txt=[20,30,33,44,55]

txt1=list(map(float,txt))

for i in txt:
    txt1.append(float(i))
print(txt1)


# for loop is used but need  to qrite multiple lines

print("this s a list:-", txt1)


# if i want to any value from the list and do it double of itt..!

double= list(map(lambda a :a * 2,txt))
print(double)
