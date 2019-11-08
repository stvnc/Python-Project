def findFpb(param, param2):
    if param > param2:
        smaller = param2
    else:
        smaller = param
    for i in range(1, smaller+1):
        if((param%i==0) and (param2%i==0)):
            fpb = i
    return fpb

def findFpbEuclidean(param, param2):
    while param2:
        param,param2 = param2, param%param2
    return param

def findKPK(param, param2):
    if param > param2:
        greater = param
    elif param < param2:
        greater = param2
    
    while(True):
        if((greater%param==0) and (greater%param2==0)):
            kpk = greater
            break
        greater+=1
    return kpk

userInput1 = int(input('Masukkan angka pertama: '))
userInput2 = int(input('Masukkan angka kedua: '))
print(findKPK(userInput1, userInput2))
print(findFpb(userInput1, userInput2))
print(findFpbEuclidean(userInput1, userInput2))
