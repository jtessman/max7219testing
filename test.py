from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.legacy import text
from luma.core.legacy.font import proportional, LCD_FONT
from luma.led_matrix.device import max7219
from open_eye import eye
import time

serial = spi(port=0, device=0, gpio=noop(), block_orientation=-90)
device = max7219(serial, width=8, height=32)

x = 0

test = eye

def draw_eye():
    with canvas(device) as draw:
        for i in test.opencoords:
            for j in range(i[1], i[2]):
                draw.point((i[0], j), fill = "white")

def draw_close_eye():
    with canvas(device) as draw:
        for i in test.closedcoords:
            for j in range(i[1], i[2]):
                draw.point((i[0], j), fill = "white")

def clean_close_eye():
    with canvas(device) as draw:
        for i in test.closedcoords:
            for j in range(i[1], i[2]):
                draw.point((i[0], j), fill = "black")

def clean_eye():
    with canvas(device) as draw:
        for i in test.opencoords:
            for j in range(i[1], i[2]):
                draw.point((i[0], j), fill = "black")

draw_eye()

while 1:
    x = x + 1
    if (x % 20) == 1:
        clean_eye()
        draw_close_eye()
    elif (x % 20) == 2:
        clean_close_eye()
        draw_eye()
    time.sleep(.2)

