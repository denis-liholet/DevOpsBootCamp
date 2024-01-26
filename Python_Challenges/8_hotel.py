# You have been asked to write a program that will show a hotel whether guests want a single room,
# a double/twin room or a family room. If there is only 1 person staying then they get a single room,
# if there are 2 people staying then they get a double/twin room and
# if there are more than 2 people staying then they get a family room.
# Your program should allow the hotel staff to enter the number of guests staying in the room.

def get_guests() -> int:
    try:
        num_of_guests = int(input("Please enter the number of guests: "))
    except ValueError:
        print("Error. Input values should be numbers only!")
        return 0

    if num_of_guests <= 0:
        print("Error. Number of guests should be grater than '0'.")
        return 0

    return num_of_guests


def onboarding() -> None:
    guests = get_guests()
    if not guests:
        return
    if guests == 1:
        print("Offer to guest a SINGLE room")
    elif guests == 2:
        print("Offer to guests a DOUBLE/TWIN room")
    else:
        print("Offer to guests a FAMILY room")


if __name__ == "__main__":
    onboarding()
