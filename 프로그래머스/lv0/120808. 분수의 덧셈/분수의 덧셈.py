def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)

def solution(numer1, denom1, numer2, denom2):
    parent = denom1 * denom2
    child = (numer1 * denom2) + (denom1 * numer2)
    g = gcd(parent, child)
    return [child / g, parent / g]