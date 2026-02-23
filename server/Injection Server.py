import socket
from pynput.keyboard import Controller, Key

keyboard = Controller()

UDP_IP = "0.0.0.0"
UDP_PORT = 4210          # Keep it same

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print(f"Listening on UDP {UDP_IP}:{UDP_PORT} ...")

pressed = set()   # track keys currently held

def hold(key):
    if key not in pressed:
        keyboard.press(key)
        pressed.add(key)
        print("DOWN:", key)

def release(key):
    if key in pressed:
        keyboard.release(key)
        pressed.remove(key)
        print("UP:", key)

while True:
    data, addr = sock.recvfrom(64)
    msg = data.decode().strip()

    # BUTTONS (still tap type)
    if msg == "H": keyboard.press("h"); keyboard.release("h")
    if msg == "J": keyboard.press("j"); keyboard.release("j")
    if msg == "K": keyboard.press("k"); keyboard.release("k")
    if msg == "L": keyboard.press("l"); keyboard.release("l")

    # JOYSTICK UPDATES
    # msg examples: "W", "A", "S", "D", "WA", "WD", "SA", "SD", "CENTER"
    active = set()

    if "W" in msg: active.add("w")
    if "A" in msg: active.add("a")
    if "S" in msg: active.add("s")
    if "D" in msg: active.add("d")

    # release keys no longer active
    for k in list(pressed):
        if k not in active:
            release(k)

    # hold currently active keys
    for k in active:
        hold(k)
