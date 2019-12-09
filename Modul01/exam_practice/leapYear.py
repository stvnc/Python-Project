def leapYear(param):
    if param % 4 == 0:
        if param % 100 == 0:
            if param % 400 == 0:
                print("Leap year")
    else: 
        print("Not leap year")

leapYear(int(input('Masukkan tahun yang ingin dicek: ')))