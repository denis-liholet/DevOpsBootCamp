hero_name = "Denys"  # String
hero_age = 28       # Integer
hero_power = 9.5    # Float

villain_name = "Async"  # String
villain_power = 8.2      # Float

# Story
print(f"\nOnce upon a time, in the magical land of Pythonia, there lived a brave hero named {hero_name}.")
print(f"{hero_name}, aged {hero_age}, possessed a mighty power level of {hero_power}.")

print(f"One day, a notorious villain named {villain_name} emerged, with a power level of {villain_power}.")
print(f"{villain_name} sought to conquer Pythonia and unleash chaos across the kingdom.")

# Action
if hero_power > villain_power:
    print(f"{hero_name} faced {villain_name} in an epic battle and emerged victorious!")
    print(f"{hero_name} used their incredible power to restore peace to Pythonia.")
else:
    print(f"{hero_name} realized the strength of {villain_name} was too formidable.")
    print(f"{hero_name} trained hard to increase their power level and prepare for the ultimate showdown.")

# Conclusion
print("In the end, Pythonia was saved, thanks to the bravery and determination of our hero,", hero_name)
