def BinPow(a, n, f):
    if n == 1:
        return a
    else:
        return f(BinPow(a, n//2, f), BinPow(a, n//2 + n % 2, f))
