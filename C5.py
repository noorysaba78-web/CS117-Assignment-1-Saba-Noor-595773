#Star _ delta transformation
def star_to_delta(ra,rb,rc):
    n=ra*rb+rb*rc+rc*ra
    return(round(n/ra,2),round(n/rb,2),round(n/rc,2))
print(star_to_delta(10,20,30))
