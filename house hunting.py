
#This is a program to calculate how many months it will take you to save up enough money for a down payment
#Assume that your investments earn a return of 4%

annual_salary = int(input("Enter your annual salary:"))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal:"))
total_cost = int(input("Enter the cost of your dream home:"))

portion_down_payment = 0.25 #we assumed that down payment will be %25 of total cost. Make it 1 if you want to calculate for total cost.
down_payment = total_cost * portion_down_payment
current_savings = 0
r = 0.04 #assuming that your invesments earn a return of 0.04 each month
monthly_salary = annual_salary / 12
monthly_saved = monthly_salary * portion_saved

number_of_months = 0
while current_savings < down_payment:
    current_savings += monthly_saved + current_savings * r / 12
    number_of_months += 1

print("Number of months:", str(number_of_months))
