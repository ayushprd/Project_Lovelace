def NAND(A, B):
    nand = 0
    if A == 0 and B == 0:
        nand = 1
    elif A == 0 and B == 1:
        nand = 1
    elif A == 1 and B == 0:
        nand = 1
    elif A == 1 and B == 1:
        nand = 0
        
    return nand
