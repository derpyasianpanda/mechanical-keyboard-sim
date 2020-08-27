import threading
from os import walk
import keyboard as kb
from time import sleep
from random import choice
from playsound import playsound

print("Welcome to the Mechanical Keyboard Simulator!\n")

isChoosing = True
while isChoosing:
    print("Please choose a directory with all the sounds (Number or Name)")
    (_, dirnames, _) = next(walk("sounds"))
    for index, name in enumerate(dirnames):
        print(str(index + 1) + ": ", name)

    user_input = input("> ")
    sound_folder = "sounds/"

    try:
        user_input = int(user_input) - 1
        if user_input < len(dirnames) and user_input > -1:
            sound_folder += dirnames[user_input]
    except ValueError:
        if user_input in dirnames:
            sound_folder += user_input

    (_, _, filenames) = next(walk(sound_folder))
    filenames = [name.split(".")[0] for name in filenames if "_" not in name]
    if not filenames:
        print("There are no sounds in this folder! :(\n")
        sleep(.75)
    else:
        isChoosing = False

print("\nWould you like to log your keys (It might lag)? (y/N)")
isLogging = input("> ").lower() == "y"

# This prevents sound spamming by holding down a key
pressed_keys = set()


def on_event(event):
    # Key name is lowercased b/c Shift+'letter' results in a capital name
    key = event.name.lower()
    if event.event_type == kb.KEY_DOWN:
        if key not in pressed_keys:
            threading.Thread(
                target=playsound,
                args=(sound_folder + f"/{key if key in filenames else choice(filenames)}.mp3", ),
                daemon=True
            ).start()
            pressed_keys.add(key)
    elif event.event_type == kb.KEY_UP:
        if key in pressed_keys:
            pressed_keys.remove(key)


if isLogging:
    kb.hook(lambda e: print(e.event_type, e.name))
kb.hook(on_event)

print("\nEnjoy your Keyboard sounds! (Press ctrl+q to quit)")
kb.wait("ctrl+q")
print("Application Ended")
