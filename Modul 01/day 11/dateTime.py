import dateTimeRef as dt

hariInIndo = {
    'Monday'   : 'Senin',
    'Tuesday'  : 'Selasa',
    'Wednesday': 'Rabu',
    'Thursday' : 'Kamis',
    'Friday'   : 'Jumat',
    'Saturday' : 'Sabtu',
    'Sunday'   : 'Minggu'
}

bulanInIndo = {
    'January'  : 'Januari',
    'February' : 'Februari',
    'March'    : 'Maret',
    'April'    : 'April',
    'May'      : 'Mei',
    'June'     : 'Juni',
    'July'     : 'Juli',
    'August'   : 'Agustus',
    'September': 'September',
    'October'  : 'Oktober',
    'November' : 'November',
    'December' : 'Desember'
}

class dateTime():
    def __init__(self):
        self.day = hariInIndo.get(dt.day) 
        # untuk mendapatkan value -> hariInIndo.get(dt.day)
        # untuk mendapatkan key -> list(hariInIndo.keys())[list(hariInIndo.values()).index(dt.day)] 
        self.date = dt.date
        self.month = bulanInIndo.get(dt.month)
        self.year = dt.year
        self.hour = dt.hour
        self.minute = dt.minute
        self.second = dt.second

print(vars(dateTime()))
