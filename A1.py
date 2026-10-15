#Fuse checked Question
V=int(input("enter voltage:"))
R=int(input("enter resistance:"))
if R<=0:
    print("invalid resistance")
else:
    I=V/R
    print("current=A")
if I>2:
    print("Fuse will below")
else:
     print("circuit is safe")
