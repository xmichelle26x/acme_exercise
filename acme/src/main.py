from utils import *
from data.constants import *


def employee_hours_pay(time, hours, pay_hours):
    time = split_time(time)
    hours_arr = []
    for h in hours: 
        hours_arr.append(split_time(h))  
    total_hours = time[1].hour - time[0].hour
    hours_normal_pay = 0 
    pay_dict = pay(hours, pay_hours)

    for i in range(len(hours_arr)):
        if time[0]  >= hours_arr[i][0] and time[1] <= hours_arr[i][1]:
            hours_normal_pay =  float(pay_dict[hours[i]])
            break
    return (hours_normal_pay, total_hours)

        

def employee_final_pay(input, hours, pay_hours ):
    file = read_file(input)
    for employee in file:
        data = employee.split('=')
        employee_name = data[0]
        employee_worked_days = data[1].split(',')
        pay = 0
        for worked_day in employee_worked_days:
            pay_days = worked_day[2:]
            hours_price_normal = employee_hours_pay(pay_days, hours, pay_hours)
            if worked_day[0:2] in days:
                pay += hours_price_normal[0]*hours_price_normal[1]
            else:
                pay += (hours_price_normal[0] + 5)*hours_price_normal[1]
        print("The amount to pay {0} is: {1} USD".format(employee_name, pay))
    
    
if __name__ == '__main__':
    print("-----------------------ACME---------------------")
    print("Hi, this is ACME company pay for hours program")
    print("------------------------------------------------\n")
    (employee_final_pay(input_file, hours, pay_hours))