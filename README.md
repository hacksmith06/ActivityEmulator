# ActivityEmulator
Automates random mouse movements, clicks, and keyboard typing to simulate user activity.

## Code Overview

This Python script automates mouse movements and keyboard actions. Its main purpose is to create seemingly random user interactions with the computer.

### Libraries Used:
- **pyautogui**: Used for automating mouse movements and keyboard actions.
- **time**: Provides sleep functions to pause the execution of the script.
- **random**: Generates random numbers and choices.
- **pynput**: Monitors and controls input devices (specifically, the keyboard in this script).

### Key Components:

1. **Global Variable**:
    - `stop_script`: This is a flag to determine when to stop the script. It gets set to True when the escape key is pressed.

2. **Keyboard Listener**:
    - The function `on_key_release` checks for the release of the escape key to stop the script. An instance of `keyboard.Listener` continuously monitors the keyboard for this event.

3. **Functions for Automation**:
    - `random_mouse_movement()`: Moves the mouse to a random position on the screen.
    - `random_keyboard_typing()`: Types random characters from a given set of alphabets and numbers.
    - `actions()`: Orchestrates random mouse and keyboard actions like clicking, double-clicking, scrolling, moving the mouse, and typing.

4. **Tab Alternating (based on the provided positions)**:
    - There is a list named `positions` that contains tuples representing x, y coordinates. The script randomly selects one of these positions, moves the mouse there, clicks, and then performs random actions.

5. **Main Loop**:
    - The main while-loop continues to run until the `stop_script` flag becomes True (i.e., until the escape key is pressed). Within this loop, the script performs the following actions in order:
        - Checks the `stop_script` flag.
        - Chooses a random position from the `positions` list.
        - Moves the mouse to that position and clicks.
        - Executes random actions using the `actions()` function.
