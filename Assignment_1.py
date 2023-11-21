def multiply(x,y):
    if x < 10 and y < 10:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby2 = n // 2
        a = x // 10**(nby2)
        b = x % 10**(nby2)
        c = y // 10**(nby2)
        d = y % 10**(nby2)
        ac = multiply(a,c)
        bd = multiply(b,d)
        return ((10**n)*ac + (10**nby2)*(a*d+b*c) + bd)
    
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
print("The product of two numbers is: ",multiply(x,y))

