import _datetime

current_datetime=_datetime.datetime.now()

print("year:",current_datetime.year)
print("month:",current_datetime.month)
print("day:",current_datetime.day)
print("hour:",current_datetime.hour)
print("minute:",current_datetime.minute)
print("second:",current_datetime.second)
print("microsecond:",current_datetime.microsecond)


current_date=_datetime.datetime.now().date()

print("year:", current_date.year)
print("month:", current_date.month)
print("day:", current_date.day)

current_date=_datetime.datetime.now().time()
print("hour:",current_date.hour)
print("minute:",current_date.minute)
print("second:",current_date.second)
print("microsecond:",current_date.microsecond)


specific_date = _datetime.date(2024, 4, 5 )

specific_time = _datetime.time(12, 30, 0)

format_date = specific_date.strftime('%d,%t,%y')

print(format_date)