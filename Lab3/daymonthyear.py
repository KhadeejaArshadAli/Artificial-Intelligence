#. a Python program to extract year, month, date and time using Lambda. 
import datetime
def DayMonthYear():
 currentDateTime = datetime.datetime.now()
 print(currentDateTime)
 year = lambda x: x.year
 month = lambda x: x.month
 day = lambda x: x.day
 print('Year - ',year(currentDateTime))
 print('Month - ',month(currentDateTime))
 print('Day - ',day(currentDateTime))


 

DayMonthYear()