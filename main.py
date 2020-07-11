from playsound import playsound
import keyboard as kb
from os import walk
from random import choice


(_, dirnames, _) = next(walk("sounds"))

current_folder = "sounds/nkcreams_glarses"
(_, _, filenames) = next(walk(current_folder))
filenames = [name.split(".")[0] for name in filenames if "_" not in name]
pressed_keys = set()
isLogging = False


def on_event(event):
    key = event.name.lower()
    if event.event_type == kb.KEY_DOWN:
        if key not in pressed_keys:
            playsound(
                f"{current_folder}/{key if key in filenames else choice(filenames)}.mp3",
                block=False
            )
            pressed_keys.add(key)
    elif event.event_type == kb.KEY_UP:
        if key in pressed_keys:
            pressed_keys.remove(key)


if isLogging:
    kb.hook(lambda e: print(e.event_type, e.name))
kb.hook(on_event)

print("Enjoy your kb sounds!")
kb.wait("esc")
print("Application Ended")
