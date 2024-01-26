current_savings = 0
portion_down_payment = 0.25
month_counter = 0

try:
    annual_salary = float(input("Enter your starting annual salary: "))
    portion_saved_per = float(input("Enter the percent of your salary to save, as decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))
except ValueError:
    print("Values should be given as numbers")
    exit(0)

target = total_cost * portion_down_payment

while current_savings < target:
    portion_saved = portion_saved_per * (annual_salary / 12)
    current_savings += current_savings * (0.04 / 12)
    current_savings += portion_saved
    month_counter += 1
    if month_counter % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print(f"Number of months: {month_counter}")
