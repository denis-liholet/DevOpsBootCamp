# You have been asked to write a program that will show the starting price for a taxi firm.
# Depending on the number of passengers there will be a different start price for the journey.
# For 1 person the start price is £2.50, for 2 people it will be £3.00, for 3 people it will be £3.50
# for 4 people it will be £4.00 and for 5 or more there is a flat rate charge of £5.00.
# Your program should allow the driver to enter the number of passengers and tells them how much the starting fare is.

start_price = {
  1: "2.50",
  2: "3.00",
  3: "3.50",
  4: "4.00",
  5: "5.00"
}


def get_passengers() -> int:
    try:
        num_of_passengers = int(input("Please enter the number of passengers: "))
    except ValueError:
        print("Error. Input values should be numbers only!")
        return 0

    if num_of_passengers <= 0:
        print("Error. Number of passengers should be grater than '0'.")
        return 0

    return num_of_passengers


def onboarding() -> None:
    passengers = get_passengers()
    if not passengers:
        return
    fare = start_price.get(passengers)
    if not fare:
        print("Starting fare is £5.00")
    else:
        print(f"Starting fare is £{fare}")


if __name__ == "__main__":
    onboarding()
