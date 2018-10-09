import glob
import os

path = 'C:\\Users\\hpadmin\\Desktop\\august'
extension = 'xlsx'
os.chdir(path)
metrics = []
vacation_dates = []
time_sheet = []
result = [i for i in glob.glob('*.{}'.format(extension))]
emails = {}
for employee in result:
    emails[employee] = 'th'
print(emails)
