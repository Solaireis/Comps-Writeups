
def solve():
    # main code here
    n = input()
    n = int(float(n))
    if n >= 1900:
        print("Division 1")
    elif n >= 1600:
         print("Division 2")
    elif n >= 1400:
        print("Division 3")
    else:
        print("Division 4")
        

def main():
    haveTestCases = 1 # change accordingly
    testCase = 1
    if (haveTestCases):
        testCase = int(float(input()))
    

    for i in range(testCase):
        solve()

main()