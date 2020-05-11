import os

def main():
    salary_file = 'salary.txt'

    with open(salary_file) as file:
        line = file.readline()
        count = 1
        while line:
            print(line)
            line = file.readline()
            count = count + 1
    
main()