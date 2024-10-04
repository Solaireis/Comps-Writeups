'''
given a number, rearrange the digits in the number based on a given pivot

if bigger, move to the left of the pivot
if same, put in the middle with the pivot
if smaller, move to the right of the pivot
*note must preserve the original order in the given number (edited)

'''

def rearrange_digits(num: int, pivot: int) -> int:

    num = int(num)
    pivot = int(pivot)

    # verifies if number is negative, if so, make it positive
    isNegative = False
    if num < 0:
        num = -num
        isNegative = True

    # converts number to list of digits, and initialises left and right hand sides
    num = [int(q) for q in str(num)] 
    left = []
    right = []

    # sorts the digits into left and right hand sides
    for i in range(len(num)):
        if num[i] > pivot:
            left.append(num[i])
        elif num[i] == pivot:
            pass
        else:
            right.append(num[i])

    # arranges the digits into the correct order
    num = left + [pivot] + right
    num = [str(q) for q in num]
    num = int(''.join(num))
    
    # converts number to negative if it was negative originally
    if isNegative:
        num = -num

    return num
    

def main():
    print(" Welcome to rearrange_digits()")
    num , pivot = input("Enter the Number and pivot, seperated by spaces: ").split()
    print("The rearranged digits 💀:  ", rearrange_digits(num, pivot))


main()