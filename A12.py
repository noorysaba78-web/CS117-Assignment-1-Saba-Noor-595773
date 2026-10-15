#parallel resistance function
def parallel_resistance(resistors):
    total=0
    for r in resistors:
        total += 1/r
    return 1/total
print(parallel_resistance([10, 10]))
   
