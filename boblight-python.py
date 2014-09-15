from lib import Boblight
import time
import ctypes

bob = Boblight()
boblightd_IP = "192.168.1.111"
boblightd_PORT = 19333

bob.bob_loadLibBoblight("/usr/local/lib/libboblight.so", "linux")

print bob.libboblight

connected = bob.bob_connect(boblightd_IP, boblightd_PORT)

def Color(r, g, b):
    rgb = (ctypes.c_int * 3)()
    rgb[0] = r
    rgb[1] = g
    rgb[2] = b
    return rgb

def Wheel(i):
    if (i < 85):
        return Color(i * 3, 255 - i * 3, 0)
    elif (i < 170):
        i -= 85
        return Color(255 - i * 3, 0, i * 3)
    else:
        i -= 170
        return Color(0, i * 3, 255 - i * 3)


if not connected:
    print("Failed to connect to boblightd")
    exit()
else:
    print("Connected to boblightd")

def demo_RGB():
    #print "r: %d, g: %d, b: %d", (r, g, b)
    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(255, 0, 0))
    time.sleep(1)

    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color(0, 255, 0))
    time.sleep(1)

    bob.bob_set_priority(128)
    bob.bob_set_static_color(Color( 0, 0, 255))
    time.sleep(1)

def rainbow():
    for i in range(0, 255):
        bob.bob_set_priority(128)
        bob.bob_set_static_color(Wheel( (i) % 255 ))
        time.sleep(0.1)

def swipe(color):
    for i in range(1, 10):
        bob.bob_addpixel(color)
        bob.bob_set_priority(128)
        bob.bob_sendrgb()
        time.sleep(1)

def test():
    width = 24
    height = 13
    bob.bob_setscanrange(width, height)
    for y in range(height):
        for x in range(width):
            bob.bob_addpixelxy(x, y, Color(x, y, 0))
    bob.bob_set_priority(128)
    bob.bob_sendrgb()

def equalizer(level):
    width = 26
    height = 13
    bob.bob_setscanrange(width, height)
    for y in range(height):
        for x in range(width):
            if y < level:
                bob.bob_addpixelxy(x, y, Color(FF, 0, 0))
    bob.bob_set_priority(128)
    bob.bob_sendrgb()

"""
while True:
    try:
        #demo_RGB()
        #rainbow()
        #swipe(Color(255, 90, 0))
        #swipe(Color(0, 90, 255))
        test()
    except KeyboardInterrupt:
        exit()
"""
