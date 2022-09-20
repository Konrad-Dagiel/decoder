def decode(n):
    i = 2
    d={}
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            d[i] = 1 + d.get(i,0)
    if n > 1:
        d[n] = 1 + d.get(n,0)
    for k in d.values():
        print(chr(k))

    return d

print(decode(324))