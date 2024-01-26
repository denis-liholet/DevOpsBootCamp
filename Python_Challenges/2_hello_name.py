# Write a program that will ask you your name
# It will then display ‘Hello Name’ where ‘Name’ is the name you have entered.

def hello(name: str) -> str:
    return f"Hello {name}"


if __name__ == "__main_":
    user_name = input("What is your name? ")
    result_string = hello(name=user_name)
    print(result_string)


# Or just one-line solution
print(f"Hello {input( 'What is your name? ')}")
