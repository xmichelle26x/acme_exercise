import datetime
import re


def read_file(path):
    with open(path) as f:
        data = f.readlines()
        return [x.strip() for x in data]

def get_employee_payment(input_data, dict_paynormal, dict_payweekend, normal_hours, weekend_hours):
    input_file = read_file(input_data)
    for employee in input_file:
        employee_name = employee.split('=')[0]
        employee_work_days = employee.split('=')[1].split(',')
        employee_pay = 0 
        for day in employee_work_days:
            pay_day = day[2::]
            hours_worked = time_string(pay_day, hours, dict_paynormal) 
            for t in day[0:2]:
                if re.match('(MO|TU|WE|TH|FR|SA|SU)', t):  
                    employee_pay += hours_worked[0]*hours_worked[1]
        output_str = 'The amount to pay {} is: {} USD'.format(employee_name,str(final_payment))
    return output_str


def dictionary_pay_normal(hours, normal_hours):
    return dict(zip(hours, normal_hours))

def dictionary_pay_weekend(hours, weekend_hours):
    return dict(zip(hours, weekend_hours))


def price_hours_worked(time_str, hours, dict_paynormal, dict_payweekend):
    time_str = time_string(time_str)
    for i in hours:
        hours_range = time_string(i)
    total_hours = end_hour.hour - start_hour.hour
    hour_price_normal = 0
    hour_price_weekend = 0

    for i in range(len(hours_range)):
        if start_hour >= hours_range[i][0] and end_hour <= hours_range[i][1]:
            hour_price_normal = float(dict_paynormal[hours[i]])
            hour_price_weekend = float(dict_payweekend[hours[i]])
            break
    return (hour_price, total_hours)


def time_string(time_str):
    time_str = time_str.split("-")
    start_hour = time_str[0]
    end_hour = time_str[1]
    time_format = '%H:%M'
    start = datetime.strptime(start_hour,time_format )
    end = datetime.strptime(end_hour, time_format)
    return (start, end)


