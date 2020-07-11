from playsound import playsound
import keyboard as kb
from os import walk
from random import choice
from time import sleep

print("Welcome to the Mechanical Keyboard Simulator!\n")

isChoosing = True;
while isChoosing:
    print("Please choose a directory (Type the number or Directory Name)")
    (_, dirnames, _) = next(walk("sounds"))
    for index, name in enumerate(dirnames):
        print(str(index + 1) + ": ", name)

    user_input = input("> ")
    desired_sounds = "sounds/";

    try:
        user_input = int(user_input) - 1
        if user_input < len(dirnames) and user_input > -1:
            desired_sounds += dirnames[user_input]
    except ValueError:
        if user_input in dirnames:
            desired_sounds += user_input

    (_, _, filenames) = next(walk(desired_sounds))
    filenames = [name.split(".")[0] for name in filenames if "_" not in name]
    if not filenames:
        print("There are no sounds in this folder! :(\n")
        sleep(.75)
    else:
        isChoosing = False

print("\nWould you like to log your keys (It might lag)? (y/N)")
isLogging = input("> ").lower() == "y"

pressed_keys = set()


def on_event(event):
    key = event.name.lower()
    if event.event_type == kb.KEY_DOWN:
        if key not in pressed_keys:
            playsound(
                f"{desired_sounds}/{key if key in filenames else choice(filenames)}.mp3",
                block=False
            )
            pressed_keys.add(key)
    elif event.event_type == kb.KEY_UP:
        if key in pressed_keys:
            pressed_keys.remove(key)


if isLogging:
    kb.hook(lambda e: print(e.event_type, e.name))
kb.hook(on_event)

print("Enjoy your Keyboard sounds! (Press the escape key to quit)")
kb.wait("esc")
print("Application Ended")
