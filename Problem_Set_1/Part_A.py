current_savings = 0
portion_down_payment = 0.25
month_counter = 0

try:
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved_per = float(input("Enter the percent of your salary to save, as decimal: "))
    total_cost = float(input("Enter the cost of your dream home: "))
except ValueError:
    print("Values should be given as numbers")
    exit(0)

portion_saved = portion_saved_per * (annual_salary / 12)
target = total_cost * portion_down_payment

while current_savings < target:
    current_savings += current_savings * (0.04 / 12)
    current_savings += portion_saved
    month_counter += 1

print(f"Number of months: {month_counter}")
