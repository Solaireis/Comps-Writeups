def solve():
    # main code here
    n = input()
    n = int(float(n))
    a = n // 1000
    b = n % 1000
    #print(a)
    #print(b)
    
    if ticket(b) == ticket(a):
        print("YES")
    else:
        print("NO")

def ticket(c):
    c1 = (c % 100 - c % 10) // 10
    c2 = c % 10
    c3 = (c % 1000 - c%100) // 100
    c4 = c1 + c2 + c3
    return c4

def main():
    haveTestCases = 1 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = int(float(input()))
    

    for i in range(testCase):
        solve()

main()