#leapyear

"""
year % 4 == 0&
year % 100 != 0/
year % 4 == 0

"""
def isLeapYear(year):
 if(year% 4==0 and year%100!=0) or year% 400==0:
   return True
 else:
   return False

year=int(input("enter a year:"))
         
if isLeapYear(year):
  print('{} is a leapyear.'.format(year))
else:
  print('{} is not a leapyear.'.format(year))