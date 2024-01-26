# You have been asked to write a program that will give the name of a shape depending on the number of sides.
# The user can only enter numbers between 3 and 8, if they enter any other number then the program should
# tell them to enter a number between 3 and 8.

def get_sides() -> int:
    try:
        num_of_sides = int(input("Please enter the number of sides: "))
    except ValueError:
        print("Error. Input values should be numbers only!")
        return 0
    if num_of_sides < 3 or num_of_sides > 8:
        print("Error. Number of sides should be from 3 to 8.")
        return 0
    return num_of_sides


def shape_name() -> None:
    sides = get_sides()
    if not sides:
        return
    match sides:
        case 3:
            print("Triangle")
        case 4:
            print("Quadrilateral")
        case 5:
            print("Pentagon")
        case 6:
            print("Hexagon")
        case 7:
            print("Heptagon")
        case 8:
            print("Octagon")


if __name__ == "__main__":
    shape_name ()
