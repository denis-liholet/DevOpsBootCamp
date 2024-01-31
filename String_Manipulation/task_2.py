from math import pi

try:
    radius = int(input("Enter the radius of the circle: "))
except ValueError:
    print("Please enter an integer.")
    exit(1)
print(f"The area of the circle with radius is "
      f"{pi * radius ** 2}")
print(f"The circumference of the circle is {2 * pi * radius}")
