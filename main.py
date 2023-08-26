import pyautogui
import time
import random
from pynput import keyboard

# Global variable to indicate when to stop the script
stop_script = False


def on_key_release(key):
    """Handle key release events."""
    global stop_script
    if key == keyboard.Key.esc:
        stop_script = True
        return False


listener = keyboard.Listener(on_release=on_key_release)
listener.start()

keyboard_controller = keyboard.Controller()


def random_mouse_movement():
    """Move mouse to a random position on screen."""
    try:
        screen_width, screen_height = pyautogui.size()
        target_x = random.randint(0, screen_width)
        target_y = random.randint(0, screen_height)
        pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.5, 2))
    except pyautogui.FailSafeException:
        print("Mouse moved to a corner of the screen. Stopping.")
        exit()


def random_keyboard_typing():
    """Type random characters using the keyboard."""
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    for _ in range(random.randint(1, 10)):
        char = random.choice(chars)
        keyboard_controller.type(char)
        time.sleep(random.uniform(0.1, 0.5))


def actions():
    """Perform random mouse and keyboard actions."""
    screen_width, screen_height = pyautogui.size()
    center_x, center_y = screen_width // 2, screen_height // 2

    try:
        pyautogui.moveTo(center_x, center_y, duration=random.uniform(0.5, 2))
        time.sleep(random.uniform(1, 5))

        action_choices = [
            'click', 'doubleClick', 'scroll', 'random_move', 'keyboard_typing'
        ]
        random_action = random.choice(action_choices)

        if random_action == 'click':
            pyautogui.click()
        elif random_action == 'doubleClick':
            pyautogui.doubleClick()
        elif random_action == 'scroll':
            pyautogui.scroll(random.randint(-10, 10))
        elif random_action == 'random_move':
            random_mouse_movement()
        elif random_action == 'keyboard_typing':
            random_keyboard_typing()

        time.sleep(random.uniform(1, 5))

    except pyautogui.FailSafeException:
        print("Mouse moved to a corner of the screen. Stopping.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")


positions = [
    (106, 22),
    (285, 26),
    (510, 33),
    (770, 21)
]

while True:
    if stop_script:
        print("ESC key pressed. Stopping the script.")
        listener.stop()
        break

    pos = random.choice(positions)
    try:
        pyautogui.moveTo(pos[0], pos[1], duration=random.uniform(0.5, 2))
        pyautogui.click()
        actions()
    except pyautogui.FailSafeException:
        print("Mouse moved to a corner of the screen. Stopping.")
        exit()
    except Exception as e:
        print(f"An error occurred: {e}")
