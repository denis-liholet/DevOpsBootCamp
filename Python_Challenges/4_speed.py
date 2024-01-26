# Improve the last program to tell you the speed you would have to travel
# at in order to go a distance within a certain time entered by the user.

def is_decimal_valid(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def speed_work_out() -> str:
    distance = input("Enter the distance as a decimal number (km): ")
    time = input("Enter the time you would have to spend (minutes): ")
    if not (is_decimal_valid(distance) and is_decimal_valid(time)):
        return "Check the entered values - they should be integers."
    speed = int(distance) / (int(time) / 60)
    return f"You need to move at a speed of {speed} km/h " \
           f"to cover {distance} km in {time} minutes"


if __name__ == "__main__":
    result = speed_work_out()
    print(result)
