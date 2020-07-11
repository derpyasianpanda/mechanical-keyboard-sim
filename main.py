from playsound import playsound
import keyboard
from os import walk

current_folder = "sounds\\nkcreams_glarses"
(dirpath, dirnames, filenames) = next(walk(current_folder))
filenames = [name.split(".")[0] for name in filenames]
pressed_keys = set()
isLogging = True


def hook_on_event(event):
    key = event.name.lower()
    if (isLogging):
        print(event.event_type, key)
    if event.event_type == keyboard.KEY_DOWN:
        if key not in pressed_keys:
            playsound(
                f"{current_folder}\\{key if key in filenames else 'a'}.mp3",
                block=False
            )
            pressed_keys.add(key)
    elif event.event_type == keyboard.KEY_UP:
        if key in pressed_keys:
            pressed_keys.remove(key)

keyboard.hook(hook_on_event)
keyboard.wait()