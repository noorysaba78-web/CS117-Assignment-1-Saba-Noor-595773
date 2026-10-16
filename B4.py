#continous discharge analysis
voltages=[12.6,12.5,12.5,12.3,12.1,11.9,12.0,11.8,11.6,11.5,11.5,11.2]
best_len=1
best_start=0
start=0
for i in range(1,len(voltages)):
    if voltages[i]>=voltages[i-1]:
        start=i
        length=i-start+1
        if length>best_len:
            best_len=length
            best_start=start
print('longest streak:',best_len,'readings')
print('started at',voltages[best_start],'v')
print('ended at',voltages[best_start+best_len-1],'v')
