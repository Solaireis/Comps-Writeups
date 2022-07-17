def solve():
    # main code here
    n = input() #input no of candles
    n = int(float(n))
    print(quantity(n))

def quantity(n):
    l = []
    i = input() 
    for k in i.split():
        b = int(float(k))
        l.append(b)
    s = min(l)
    #print(s)
    l.pop(l.index(s))
    #print(l)
    a = 0
    for i in range(len(l)):
        a += l[i]
    #print(a)
    a -= (n-1) * s
    return a

def main():
    haveTestCases = 1 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = int(float(input()))
    

    for i in range(testCase):
        solve()

main()