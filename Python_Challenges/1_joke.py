# Write a program that will display a joke
# Don’t display the punchline until the reader hits an appropriate key.

from time import sleep

JOKE_START = "Why do programmers prefer dark mode?"
PUNCHLINE = " Because light attracts bugs."


def get_joke() -> None:
    print(JOKE_START)
    pressed_button = input("Press 'Y'+'Enter' to reveal the punchline... ")
    if pressed_button.upper() != 'Y':
        print("No punchline at this time. Try to hit 'Y' key next time.")
        return
    for _ in range(3):
        print(".", end='')
        sleep(0.5)
    print(PUNCHLINE)


if __name__ == "__main__":
    get_joke()
