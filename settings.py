#!/usr/bin/env python2
from lib import Boblight
import ctypes

# Settings
# will/should be replaced with command line options
boblightd_IP = "192.168.1.111"
boblightd_PORT = 19333
boblightd_PRIORITY = 128

bob = Boblight()

bob.bob_loadLibBoblight("/usr/local/lib/libboblight.so", "linux")

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
