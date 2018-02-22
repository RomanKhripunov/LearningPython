from datetime import date, timedelta

res_date = date(*[int(i) for i in input().split()]) + timedelta(int(input()))
print(res_date.year, res_date.month, res_date.day)
res_date.strftime()