# Write a program that asks the user to input their age.
# If the user is 18 or over it should output “You are old enough to vote”.
# Otherwise it should output “You are not old enough to vote”.

age = input("How old are you? ")
if not age.isdigit():
    print("Error. Please enter decimal number.")
elif int(age) >= 18:
    print("You are old enough to vote.")
else:
    print("You are not old enough to vote.")
