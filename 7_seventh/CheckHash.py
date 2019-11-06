def getHash(num, f, mod):
    return f(num) % mod

def checkhash(seq, f, mod):
    hashes = {}
    for i in seq:
        h = getHash(i, f, mod)
        if h not in hashes:
            hashes[h] = 0
        hashes[h] += 1

    return (max(hashes.values()), min(hashes.values()))