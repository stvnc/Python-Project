import requests

userInput = input('Masukkan kode bank yang diinginkan: ')
url = f'https://kurs.web.id/api/v1/{userInput}'
data = requests.get(url)
rate = data.json()

bankList = ['bca', 'bi', 'bjb', 'bni', 'bri', 'btn', 'bukopin', 'cimb', 'commonwealth', 'danamon', 'hsbc', 'jtrust', 'mandiri', 'mayapada', 'maybank',
            'mega', 'muamalat', 'ocbc', 'panin', 'permata', 'sinarmas', 'uob', 'wooribersaudara']

if userInput not in bankList:
    print('Bank tidak tersedia')
else:
    print('Pilih opsi:')
    print('1. USD => IDR')
    print('2. IDR => USD')
    print('3. USD => BTC')
    print('4. IDR => BTC')
    choiceInput = int(input('Pilih 1, 2, 3, atau 4: '))
    valueInput =  int(input('Masukkan nominal: '))

    if choiceInput == 1:
        valueRetrieve = int(rate["beli"]) * valueInput
        print(f"Hasil konversi US$ {valueInput} adalah Rp. " + str(valueRetrieve))

    elif choiceInput == 2:
        valueRetrieve = valueInput / int(rate["jual"])
        print('%0.2f' %valueRetrieve + " USD")

    elif choiceInput == 3:
        blockchainUrl = f"https://blockchain.info/tobtc?currency=USD&value={valueInput}"
        bcData = requests.get(blockchainUrl)
        bcRate = bcData.json()
        print(f'Hasil konversi US$ {valueInput} adalah {bcRate} BTC')
        
    else:
        valueRetrieve = valueInput // int(rate["jual"])
        blockchainUrl = f"https://blockchain.info/tobtc?currency=USD&value={valueRetrieve}"
        bcData = requests.get(blockchainUrl)
        bcRate = bcData.json()
        print(f'Hasil konversi Rp. {valueInput} adalah {bcRate} BTC')

        
        


