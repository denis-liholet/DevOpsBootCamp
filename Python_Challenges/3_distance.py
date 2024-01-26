# Write a program that will work out the distance travelled if the user enters in the speed and the time.

def is_decimal_valid(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False


def distance_work_out() -> str:
    speed = input("Enter your speed as a decimal number (km/h): ")
    time = input("Enter the time you spent to travel (minutes): ")
    if not (is_decimal_valid(speed) and is_decimal_valid(time)):
        return "Check the entered values - they should be integers."
    distance = (int(time) / 60) * int(speed)
    return f"The distance covered is {distance} km"


if __name__ == "__main__":
    result = distance_work_out()
    print(result)
