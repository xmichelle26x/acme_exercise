import datetime
from os import read
import re

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



def employee_total_hours():
    print("hello")

def employee_data(input):
    file = read_file(input)
    for e in file:
        employee = e.split('=')
        employee_name = employee[0]
        employee_worked_days = employee[1].split(',')



    print(employee_name) 
    print(employee_worked_days) 
employee_data('data/data.txt')



