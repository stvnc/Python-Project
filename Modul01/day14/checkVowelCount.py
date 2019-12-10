# string of vowels
vowels = 'aeiou'
ip_str = 'Hello, have you tried our tutorial section yet?'
# make it suitable for caseless comparisions
ip_str = ip_str.casefold()
# make a dictionary with each vowel a key and value 0
count = {}.fromkeys(vowels,0)
# count the vowels
for char in ip_str:
   if char in count:
       count[char] += 1
print(count)


vowelDict = {}

for i in vowels:
        vowelDict.setdefault(i, 0)
for i in ip_str:
    count = 0
    if i in vowels:
        vowelDict[i] += 1

print(vowelDict)