#current and power function
def ohm_current(v,r):
    return v/r
def power_dissipated(i,r):
    return i*i*r
v=12
r=6
current=ohm_current(v,r)
power=power_dissipated(current,r)
print("current=",current,"A")
print("power=",power,"W")

