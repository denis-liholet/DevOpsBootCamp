money_received = 0

salary = int(input("Enter your Salary: "))

if salary > 10600:
    tax_free_salary = 10600
    taxable_salary = salary - 10600
else:
    tax_free_salary = salary
    taxable_salary = 0

if taxable_salary > 0:
    money_received = tax_free_salary + (taxable_salary * 0.8)
    print(f"After tax you would receive {money_received}")
else:
    money_received = tax_free_salary
    print(f"You would receive {money_received}. Not tax applied.")
