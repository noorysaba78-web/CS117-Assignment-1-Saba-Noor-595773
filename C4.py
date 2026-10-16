def loaded_divider(vs, r1, r2, r3):
    v_unloaded=vs *r2/(r1+r2)
    rp=r2*r1/(r2+r1)
    v_loaded=vs*rp/(r1+rp)
    return v_unloaded, v_loaded
print(loaded_divider(12,1000,1000,500))
