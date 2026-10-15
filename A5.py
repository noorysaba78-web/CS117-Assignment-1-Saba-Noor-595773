#smallest and largest resistor
x=int(input("enter a number"))
y=int(input("enter a number"))
z=int(input("enter a number"))
if x > y and y > z:
    print("largest value is R1",x)
    print("samllest value is R3",z)
elif y > z and z > x:
    print("largest value is R2",y)
    print("smallest value is R1",x)
elif z > x and x > y:
    print("largest value is R3",z)
    print("samllest value is R2",y)
elif y > x and x > z:
    print("largest value is R2",y)
    print("smallest value is R3",z)
elif z> y and y > x:
    print("largest value is R3",z)
    print("samllest value is R1",x)
elif x > z and z > y:
    print("largest value is R1",x)
    print("samllest value is R2",y) 
else:
    print("invalid")
