from datetime import datetime 
from data.constants import hours,pay_hours

def read_file(path):
    with open(path) as f:
        employees_list = []
        data = f.readlines()
        for i in data:
            employees_list.append(i.strip())
        return employees_list    
        

def split_time(time):
    time = time.split('-') 
    time_format = '%H:%M'
    initial_time = datetime.strptime(time[0],time_format).time()
    end_time = datetime.strptime(time[1], time_format).time()
    return (initial_time, end_time)

def pay(hours, pay_hours):
    return dict(zip(hours, pay_hours)) 

# print(pay(hours,pay_hours))