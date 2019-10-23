#This is a program to calculate how many months it will take you to save up enough money for a down payment with a raise
#Assume that your investments earn a return of 4% each year

annual_salary = int(input("Enter your starting annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal:"))

portion_down_payment = 0.25 #assume
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04 #assuming that your invesments earn a return of 0.04 each year

number_of_months = 0

while current_savings < down_payment:
    monthly_salary = annual_salary / 12
    monthly_saved = monthly_salary * portion_saved
    current_savings += monthly_saved + current_savings * r / 12
    number_of_months += 1
    if number_of_months % 6 == 0:
        annual_salary = annual_salary + annual_salary * semi_annual_raise

print("Number of months:", str(number_of_months))