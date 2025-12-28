#!/usr/bin/env python3
import sys, subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QVBoxLayout
from PyQt5.QtCore import Qt
#import os
#os.environ["QT_LOGGING_RULES"] = "*.warning=false"  # STFU Qt warnings

app = QApplication(sys.argv)

w = QWidget()
#w.setWindowTitle("*")
w.setFixedSize(20, 120)

slider = QSlider(Qt.Vertical)
slider.setRange(10, 120)
'''
evidently if display brigthness goes to 0, 
my machine tries to go to sleep

also interesting, is you can over drive brightness with xrandr

'''
slider.setValue(50)


def set_brightness(value):
    # int -> float  (slider% 0->100 -> 0.0-1.0 xrandr brightness)
    brightness = value / 100.0
    #print(f"{value} bights")
    OUTPUT = "HDMI-1"     #find with: $xrandr
    # xrandr --output HDMI-1 --brightness 0.7 # base command
    subprocess.run(
        ["xrandr", "--output", OUTPUT, "--brightness", str(brightness)],
        check=False
    )


layout = QVBoxLayout(w)
layout.setContentsMargins(0, 0, 0, 0)
layout.addWidget(slider)

slider.valueChanged.connect(set_brightness)

w.show()
sys.exit(app.exec_())
