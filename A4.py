#Logic gate
x=int(input("enter A"))
y=int(input("enter B"))
if x==0 or x==1 and y==0 or y==1:
    print("The result")
    if x == 1 and y ==1:
        print("AND=1")
    else:
        print("AND=0")
    if x == 0 and y == 0:
        print("OR=0")
    else:
        print("OR=1")
    if x!=y :
        print("XOR=1")
    else:
        print("XOR=0")
else:
    print("bits must be 0 or 1")
            
