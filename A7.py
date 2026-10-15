#Resistor in series
x=int(input("how many resistors in series?"))
total_resistance=0
for i in range(x):
    y=int(input("enter the resistance R"))
    total_resistance = y + total_resistance       
print(total_resistance)
                
