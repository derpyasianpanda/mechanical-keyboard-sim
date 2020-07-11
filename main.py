from playsound import playsound
import keyboard
from os import walk

current_folder = "sounds\\nkcreams_glarses"

(dirpath, dirnames, filenames) = next(walk(current_folder))
filenames = [name.split(".")[0] for name in filenames]
pressed_keys = []


def hook_on_event(event):
    if event.event_type == keyboard.KEY_DOWN:
        if event.name not in pressed_keys:
            print(event.event_type, event.name)
            playsound(
                f"{current_folder}\\{event.name if event.name in filenames else 'backspace'}.mp3",
                block=False
            )
            pressed_keys.append(event.name)
    elif event.event_type == keyboard.KEY_UP:
        print(event.event_type, event.name)
        if event.name in pressed_keys:
            pressed_keys.remove(event.name)

keyboard.hook(hook_on_event)
keyboard.wait()