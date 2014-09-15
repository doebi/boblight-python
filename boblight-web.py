#!/usr/bin/env python2
from flask import *
from lib import Boblight
import time
import ctypes

app = Flask(__name__)

# Settings
# will/should be replaced with command line options
boblightd_IP = "192.168.1.111"
boblightd_PORT = 19333
boblightd_PRIORITY = 128

color = (50, 50, 50)

bob = Boblight()
bob.bob_loadLibBoblight("/usr/local/lib/libboblight.so", "linux")
connected = bob.bob_connect(boblightd_IP, boblightd_PORT)

if not connected:
    print("Failed to connect to boblightd")
    exit()
else:
    print("Connected to boblightd")


def Color(r, g, b):
    rgb = (ctypes.c_int * 3)()
    rgb[0] = int(r)
    rgb[1] = int(g)
    rgb[2] = int(b)
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

@app.route("/")
def index():
    return render_template("/index.html", color=color)

@app.route("/set/<red>,<green>,<blue>")
def set(red, green, blue):
    print "set color to: rgb("+red+", "+green+", "+blue+")"
    color = Color(red, green, blue)
    bob.bob_set_priority(boblightd_PRIORITY)
    bob.bob_set_static_color(color)
    return "success"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
