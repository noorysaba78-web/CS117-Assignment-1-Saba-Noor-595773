#Resistor tolerance sorting
A=0
B=0
C=0
while True:
    r=float(input("enter resistance(0 to stop):"))
    if r==0:
        break
    elif 99<=r<=101:
            A=A+1
    elif 95<=r<=105:
            B=B+1
    else:
        C=C+1
print("1% tolerance:",A)
print("2% tolerance:",B)
print("rejected:",C)
