__author__="mike"
__date__ ="$27-Dec-2014 6:57:59 PM$"

"""
    Find absolute diff in days between dates
"""
from datetime import datetime
from datetime import date

def days_diff(date1, date2):
    date1 = datetime.strptime(str(date(*date1)), "%Y-%m-%d")
    date2 = datetime.strptime(str(date(*date2)), "%Y-%m-%d")
    return abs((date2 - date1).days)
    
if __name__ == "__main__":
    print(days_diff((1982, 4, 19), (1982, 4, 22))) #== 3
    print(days_diff((2014, 1, 1), (2014, 8, 27)))  #== 238
    print(days_diff((2014, 8, 27), (2014, 1, 1)))  #== 238
    print(days_diff((1,1,1), (9999,12,31)))
