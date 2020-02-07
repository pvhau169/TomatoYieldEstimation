from datetime import date
import pandas as pd


def count_date(date_planting, date_key):
    f_date_array = date_planting.split('/')
    f_date = date(int(f_date_array[2]), int(f_date_array[0]), int(f_date_array[1]))
    l_date = ''.join(s for s in date_key if s.isdigit())
    #print(int('20'+l_date[:2]), int(l_date[2:4]), int(l_date[4:6]))
    l_date = date(int('20'+l_date[:2]), int(l_date[2:4]), int(l_date[4:6]))
    return(abs((l_date-f_date).days))

data = pd.read_csv('2016_spring/2016_spring_CC.csv')
f_date = date(int('2014'), 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)
print(count_date('2/2/12', 'CC020216'))
