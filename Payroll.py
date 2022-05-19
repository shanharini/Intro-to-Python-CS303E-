# File: Payroll.py
# Student: Harini Shanmugam
# UT EID: hs28663
# Course Name: CS303E
#
# Date Created: 9/11/2021
# Date Last Modified: 9/11/2021
# Description of the Program: This program takes the user's input about their work and prints a payroll statement

print("")
name = input("Enter employee's name: ")
hoursWorked = float(input("Enter number of hours worked in a week: "))
payRate = float(input("Enter hourly pay rate: "))
federalTaxRate = float(input("Enter federal tax withholding rate: "))
stateTaxRate = float(input("Enter state tax withholding rate: "))
print("")

grossPay = hoursWorked * payRate
federalTaxWitheld = federalTaxRate * grossPay
stateTaxWitheld = stateTaxRate * grossPay
totalDeduction = federalTaxWitheld + stateTaxWitheld

print("Employee Name:", name)
print("Hours Worked:", hoursWorked)
print("Pay Rate: $" + format(payRate, "1.2f"))
print("Gross Pay: $" + format(grossPay, "1.2f"))
print("Deductions:")
print("  Federal Withholding (" + format(federalTaxRate * 100, "1.1f") + "%): $" + format(federalTaxWitheld, "1.2f"))
print("  State Withholding (" + format(stateTaxRate * 100, "1.1f") + "%): $" + format(stateTaxWitheld, "1.2f"))
print("  Total Deduction: $" + format(totalDeduction, "1.2f"))
print("Net Pay: $" + format(grossPay - totalDeduction, "1.2f"))
