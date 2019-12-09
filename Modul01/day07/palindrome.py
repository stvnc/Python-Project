def palindromeChecker(param):
    paramReversed = param[::-1]
    paramLength = len(param)
    count = 0

    for i in range(0, paramLength):
        if param[i] == paramReversed[i]:
            count += 1
        
    if count == paramLength:
        print('Palindrome')
    else:
        print('Not Palindrome')
        
def palindromeCheckerWithoutCount(param):
    paramReversed = param[::-1]
    if param == paramReversed: 
        print('Palindrome')
    else:
        print('Not Palindrome')

palindromeChecker(str(input('Masukkan kata yang ingin dicek: ')))


            