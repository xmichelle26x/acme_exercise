import datetime
from os import read 

print("Hi, this is ACME company pay for hours program")

hours = ['00:01-09:00',
        '09:01-18:00',
        '18:01-23:59']
normal_hours = [25, 15, 20]
weekend_hours =  [30, 20, 25]  
work_days = ['MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU']
weekend_days = ['SA', 'SU']


def read_file(path):
    with open(path) as f:
        employees_list = []
        data = f.readlines()
        for i in data:
            employees_list.append(i.strip())
        return employees_list
    
print(read_file('data/data.txt'))


def normal_pay(hours, normal_hours):
    return dict(zip(hours, normal_hours))

def weekend_pay(hours, weekend_hours):
    return dict(zip(hours, weekend_hours)) 



def split_time(time):
    time = time.split('-') 
    time_format = '%H:%M'
    initial_time = datetime.strptime(time[0],time_format)
    end_time = datetime.strptime(time[1], time_format)
    return (initial_time, end_time)


def employee_hours_pay(time, hours, normal_pay, weekend_pay):
    total_hours_worked = split_time(time)
    for hour in hours: 
        hours_arr = split_time(hour)
        # initial_time = time[0]
        # end_time = time[1]
        total_worked_hours = time[0] - time[1]
        hours_normal_pay = 0
        hours_weekend_pay = 0

        for h in range(len(hours_arr)):
            if time[0] >= hours_arr[h][0] and time[1] <= hours_arr[h][1]:
                hours_normal_pay = float(normal_pay[hours[h]])
                hours_weekend_pay = float(weekend_pay[hours[h]])
                break
        return (hours_normal_pay, hours_weekend_pay, total_worked_hours)


def employee_final_pay(input):
    file = read_file(input)
    for e in file:
        employee = e.split('=')
        employee_name = employee[0]
        employee_worked_days = employee[1].split(',')
        pay = 0
        for worked_day in employee_worked_days:
            pay_days = worked_day[2::]
            




