userInput1 = input('Masukkan kata yang ingin dicek: ')
userInput2 = input('Masukkan kata kedua yang ingin dicek: ')

def anagramChecker(param1, param2):
    if sorted(param1) == sorted(param2):
        print(f'{param1} and {param2} are anagram')
    else:
        print(f'{param1} and {param2} aren\'t anagram')

anagramChecker(userInput1, userInput2)