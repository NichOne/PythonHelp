"""
N+1 Automation Program - V.0.0.1 - By Malicious Coder
-----------------------------------------------------
KeyBinds
-----------------------------------------------------
P = Pause
Enter or Space = Enter new number tap twice
R = Resume
Q + Enter = End Script
"""
import pyautogui
import keyboard


def run_script():
    # Define the starting number
    start_number = 1234567

    # Set the initial clipboard value
    pyautogui.write(str(start_number))

    # Function to check if a specific key is pressed
    def is_key_pressed(key):
        return keyboard.is_pressed(key)

    # Variable to track the pause state
    paused = False

    # Variable to control script execution
    running = True

    # Loop to increment the number
    while running:
        # Check if the "p" key is pressed to toggle pause/resume
        if is_key_pressed('p'):
            paused = not paused
            if paused:
                print("Paused")
            else:
                print("Resumed")

        # Check if the process is not paused
        if not paused:
            # Wait for the user to press a key to paste the number
            while True:
                if any(is_key_pressed(key) for key in ['enter', 'space']):
                    break
                elif is_key_pressed('x'):
                    paused = True
                    print("Paused")
                    break

            # Check if the process is still paused
            if paused:
                # Wait for the user to press the resume key ("r")
                while not is_key_pressed('r'):
                    pass

                paused = False
                print("Resumed")

        # Check if the process is not paused
        if not paused:
            # Simulate pressing the Enter key to proceed
            pyautogui.press('enter')

            # Increment the number
            start_number += 1

            # Update the clipboard value with the new number
            pyautogui.write(str(start_number))

        # Check if the "Esc" key is pressed to stop the script
        if is_key_pressed('q'):
            print("Script stopped.")
            running = False


# Call the run_script() function to execute the script
run_script()
