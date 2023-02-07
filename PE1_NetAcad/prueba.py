
def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    dias=[31,28,31,30,31,30,31,31,30,31,30,31]
    total = dias[month-1]
    if month==2 and is_year_leap(year):
        total = total + 1
    return total

def day_of_year(year, month, day):
    total =0
    for i in range(month-1):        
        total = total +  days_in_month(year, i+1)
    return total+day


print(day_of_year(2000, 2, 2))
'''
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    print("dias: ",result)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
'''
