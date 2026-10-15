#Decimal to binary
def decimal_to_binary(n):
    result = " "
    while n>0:
        remainder = n%2
        result = str(remainder)+result
        n= n//2
    return result
print(decimal_to_binary(8))
print(decimal_to_binary(10))
