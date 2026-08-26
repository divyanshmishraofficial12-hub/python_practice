def gen():
    yield "1." #yield ek pause button ki tarah kaam karta hai. Yeh value return karke wahi ruk jata hai (state yaad rakhta hai) aur agli baar jab bulaya jaye toh wahi se aage chalta hai.

    yield 2
    yield 3

for x in gen():
     
    print(x, 'is a number')
    print(x, 'runs from a generator')
    print(x, 'will now move to the next YIELD number')
    print('========================================')
'''Step-by-Step Execution:

Pehli baar loop chalta hai, toh gener() function 1 yield karta hai. x ki value 1 ho jaati hai, saare print statements run hote hain.

Jab loop agli baar chalta hai, toh function shuru se start nahi hota, balki pehle wale yield 1 ke theek baad (yield 2 par) jump karta hai aur 2 deta hai.

Aise hi phir 3 ke liye hota hai.'''

