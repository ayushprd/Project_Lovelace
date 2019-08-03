def rock_temperature(S, a, e):
    T = 0
    
    T = (((1 - a) * S) / (4 * e * (5.670374419 * 10 ** -8))) ** (1 / 4)
    
    T = T - 273.15
    
    return T
