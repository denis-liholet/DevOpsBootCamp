num1 = float(input("Enter the first floating-point number (num1): "))
num2 = float(input("Enter the second floating-point number (num2): "))
decimal_places = int(input("Enter the number of decimal places: "))

sum_result = num1 + num2
product_result = num1 * num2

print(f"The sum of {num1} and {num2} is {round(sum_result, decimal_places)}")
print(f"The product of {num1} and {num2} is {round(product_result, decimal_places)}")
