import datetime
import re

hours = ['00:01-09:00',
        '09:01-18:00',
        '18:01-23:59']

normal_hours = [25, 15, 20]

weekend_hours =  [30, 20, 25]  


def read_file(input):
    with open(input,'r') as f:
        lines = []
        for line in f:
            lines.append(line)
        return lines

#print(read_file('data.txt'))
        




print("Hi, this is ACME company pay for hours program")
