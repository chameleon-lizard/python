def pigen():
    a, b, n = 4, 1, 0
    while True:
        b += 2
        n += 1
        a += (-1)**(n % 2) * 4 / b
        yield a - (-1)**(n % 2) * 4 / b
