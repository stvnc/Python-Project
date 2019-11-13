def leapYear(param):
    if param % 4 == 0:
        print("Leap year")
    else: 
        print("Not leap year")

leapYear(int(input('Masukkan tahun yang ingin dicek: ')))