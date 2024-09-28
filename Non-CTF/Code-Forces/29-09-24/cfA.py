def solve():
    n , k = input().split()
    n = int(n)
    k = int(k)
    a = input().split()
    r = 0
    c = 0
    r = int(r)
    c = int(c)
    for i in range (n):
        b = int(a[i])
        if b >= k:
            r = r + b
        if (b == 0) & (r > 0 ):
                r = r - 1
                c = c + 1

    return c

def main():
    t = input()
    t = int(t)
    a = []
    a = [0 for i in range(t)] 
    for i in range (t):
        a[i] = solve()
        print(a[i])
    
    return a

main()