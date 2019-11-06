def moar(a, b, n):
    aRes = 0
    bRes = 0
    
    for i in a:
        aRes += (i % n) == 0
    
    for i in b:
        bRes += (i % n) == 0
        
    return aRes > bRes
