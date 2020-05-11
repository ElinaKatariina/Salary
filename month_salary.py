import os
import re

def monthly_sal():
    
    count_file = 'counted.txt'

    x = []
    file_in = open('counted.txt', 'r')
    for y in file_in.read().split('\n'):
        x.append(float(y))
        sal = sum(x)
    month = input("Enter month: Jan-Dec ")

    month_sum = open("months_sal.txt", "a")
    month_sum.write(str(sal) + "  " + str(month) + "\n")
    month_sum.close()
    open("counted.txt", "w").close()
    print("Salary summary written!")
        

    return sal