import fungsiStatistik as fs
x = [1, 2, 3, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7]

print(f'Mean = {fs.findMean(x)}')
print(f'Median = {fs.findMedian(x)}')
print(f'Modus = {fs.findMode(x)}')

class hasilStatistik():
    def __init__(self):
        self.mean = fs.findMean(x)
        self.median = fs.findMedian(x)
        self.modus = fs.findMode(x)

print(vars(hasilStatistik()))