#sensor readings
x=(3.3,3.1,3.4,2.9,3.6,3.0,3.2)
highest=0
lowest=100
for i in x:
    if i > 3.2:
        print(i)
    elif i > highest:
        highest=i
    elif i < lowest:
        lowest=i
print("highest:",highest)
print("lowest:",lowest)
    
