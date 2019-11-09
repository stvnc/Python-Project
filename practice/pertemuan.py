distance = 120
speedA = 60
speedB = 40
jamMulai = 9
menit = "0"

pertemuanInJam = int(distance / (speedA+speedB))
pertemuanInMenit = int((distance % (speedA+speedB))/100 * 60)
if pertemuanInMenit < 10:
    pertemuanInMenit = str(pertemuanInMenit)
    pertemuanInMenit = menit + pertemuanInMenit    
jamPertemuan = str(jamMulai + pertemuanInJam)+":"+str(pertemuanInMenit)

print(f'Mereka akan bertemu dalam {pertemuanInJam} jam {pertemuanInMenit} menit')
print(f'Mereka akan bertemu pada pukul {jamPertemuan}')