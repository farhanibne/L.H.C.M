def find_hcf(x,y):
    while(y):
        x , y = y, x % y

    return x 

a = int(input("enter first number:  "))
b = int(input("enter second number:  "))
hcf = find_hcf(a,b)
lcm = (a * b) // hcf


print(f"The Hcf Of {a} and {b} is {hcf}")
print(f"The Lcm of {a} and {b} is {lcm}")
