import pynput

def get_coords(x, y, button, pressed):
    print((x, y))

with pynput.mouse.Listener(on_click = get_coords) as listen:
    listen.join()