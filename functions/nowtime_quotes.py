import yfinance as yf
from datetime import datetime,date
from aiogram import types
from datetime import date
import numpy as np

import arrow

# data = yf.download('AAPL','2021-05-01','2021-05-19')
# current_date = datetime.now().date()
# x = str(current_date)
#
# data = yf.download('AAPL', x)
#
# print(type(data))
# x=data['Adj Close']
# x2=len(x)
# print(x[0:0])

#получение значения котировки за последнее возможное время
def nowtime_quotes(tiker: str):
    current_date = datetime.now().date()
    x = str(current_date)
    data = yf.download(tiker, x)
    return(data['Adj Close'])

#количество рабочих дней
def work_days_between(d1, d2):
    work_days = np.busday_count(d1, d2)
    return (work_days)

print (work_days_between('2021-05-01','2021-05-18'))
def profit()


