def solve():
    #n = number of elements
    #k = the number chosen for the comparison
    n , k = input().split()
    n = int(n)
    k = int(k)

    #array of golds per person to be compared
    a = input().split()

    #robin total golds
    r = 0

    #number of times robin has to give up a gold
    c = 0

    r = int(r)
    c = int(c)

    #compares each person gold in the array to the number chosen
    for i in range (n):
        b = int(a[i])
        #if person has more gold than the number chosen, robin gets all the gold
        if b >= k:
            r = r + b

        #if person has no gold & robin has gold, robin gives up a gold
        if (b == 0) & (r > 0 ):
                r = r - 1
                c = c + 1

    return c

def main():
    #number of test cases
    t = input()
    t = int(t)

    #array to store the answers
    a = []
    a = [0 for i in range(t)] 
    for i in range (t):
        a[i] = solve()
        #for each test case, print the answer for codeforces to read
        print(a[i])
    
    return a

main()