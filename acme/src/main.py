from hours import split_time 
from data.constants import hours, pay_hours, file_path, days

print("Hi, this is ACME company pay for hours program")

def read_file(path):
    with open(path) as f:
        employees_list = []
        data = f.readlines()
        for i in data:
            employees_list.append(i.strip())
        return employees_list    
print(read_file(file_path))



def employee_hours_pay(time, hours, pay_hours):
    time = split_time(time)
    hours_arr = []
    for h in hours: 
        hours_arr.append(split_time(h))
        initial_time = time[0] 
        end_time = time[1] 
        total_hours = initial_time.hour - end_time.hour
        hours_normal_pay = 0 

        for i in range(len(hours_arr)):
            if initial_time >= hours_arr[i][0] and end_time <= hours_arr[i][1]:
                hours_normal_pay = float(pay_hours[hours_arr[i]])
                break
        return (hours_normal_pay, total_hours)

def employee_final_pay(input, hours, pay_hours ):
    file = read_file(input)
    for e in file:
        employee = e.split('=')
        employee_name = employee[0]
        employee_worked_days = employee[1].split(',')
        pay = 0
        for worked_day in employee_worked_days:
            pay_days = worked_day[2::]
            hours_price_normal = employee_hours_pay(pay_days, hours, pay_hours)
            if worked_day[0:2] in days:
                pay += hours_price_normal[0]*hours_price_normal[1]
            else:
                pay += (hours_price_normal[0] + 5)*hours_price_normal[1]
        output_str = "The amount to pay {0} is: {1} USD".format(employee_name, pay)
    return output_str


# print(employee_final_pay(file_path, hours, pay_hours))