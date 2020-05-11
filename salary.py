import salary_count
import month_salary

def main():
   laplus = 0
   print("Counting salary!")
   hours = input("Enter hours: ")
   evening = input("Enter hours after 18: ")
   wday = input("Enter day of the week (Ma-Su): ")
   if wday=="la":
         laplus = input("Enter hours after 13: ")
   superv = input("Were you supervisor? (y/n): ")
   date = input("Date: (dd.m) ")

   print(date + " salary is: ")
   salary = salary_count.counting(hours, evening, wday, laplus, superv, date)
   sala = print(round(salary, 1))

   sala_file = open("salary.txt", "a")
   sala_file.write(str(date) + " -  " + str(salary) + "€" + "\n")
   sala_file.close()
   print("Data written to salary.txt!")
   
   count_file = open("counted.txt", "a")
   count_file.write(str(salary) + "\n")
   count_file.close()
   print("Counted ok!")

main()