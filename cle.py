from pynput import keyboard

def on_press(key):
    try:
        print('アルファベットキーを押した: {0} '.format(
            key.char))
    except AttributeError:
        print('特殊キーを押した: {0}'.format(
            key))

def on_release(key):
    print('キーを離した: {0}'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()