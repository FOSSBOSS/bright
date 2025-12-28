# bright
Brightness applet doesnt work on the desktop, fix it with "xrandr --output HDMI-1 --brightness 0.7" 
but no slider. ... ok lets fix that

Lets use this article to make the applet bit
https://askubuntu.com/questions/750815/fuzzy-clock-for-ubuntu

Then track the applet down and reuse the brigthness applet icon
https://askubuntu.com/questions/419624/where-are-panel-applet-information-stored-in-mate/648427#648427

or maybe I should just track down the source code for the brightness applet. 
Im currious. its just a flipping slider, but Im currious about what it actualy does,
and why the heck it fails for real...

x11 dependent obviously.

Get display info: 
$ xrandr
Screen 0: minimum 320 x 200, current 3840 x 2160, maximum 16384 x 16384
HDMI-1 connected primary 3840x2160+0+0 (normal left inverted right x axis y axis) 1600mm x 900mm
   3840x2160     30.00*+  25.00    24.00    29.97    23.98  
   4096x2160     30.00    25.00    24.00    29.97    23.98  
   1920x1080     60.00    50.00    59.94    30.00    25.00    24.00    29.97    23.98  
   ...
HDMI-2 disconnected (normal left inverted right x axis y axis)


so this command, doesnt dim the TV, monitor, whatver, it dicounts the output.
true dimming, backlight dimming may be a function of the interface, suchas hdmi-cec
and the model of tv / monitor. The method above is to provide a means which will work,
independent of specific hardware / capabilities.

#utils for cec 
sudo apt install cec-utils

while I learned about CEC from some previous HDMI projects, I guess CEC is possible on other 
modern video sources. I havent used cec-utils yet, just reading about it.

$ cec-client 
No device type given. Using 'recording device'
CEC Parser created - libCEC version 6.0.2
no serial port given. trying autodetect: FAILED

man cec-config
man cec-client
both are sorta junk.
but maybe the util is usable.
