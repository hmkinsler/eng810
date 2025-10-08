# To be able to control my DSLR cameras on the Raspberry Pi, I followed this tutorial for installing libgphoto and gphoto2: https://pimylifeup.com/raspberry-pi-dslr-camera-control/

# I referred to this resource to understand how to write Python scripts that call gphoto2 commands: https://pypi.org/project/gphoto2/

import os # this library will allow me to write files to my machine
import subprocess # since I have used gphoto2 from the Raspberry Pi terminal, I am using subprocess here to outline the command prompt lines that I would use to control my camera
from settings import capture_directory # this ensures that I can easily change the directory that I want to write photos to across different machines

def capture_page():
    num_captures = 1, # default number of images captured is 1
    ISO = 100, # default camera ISO is 100
    aperture = 11.0 # default aperture is 11.0
    shutter = 250 # default shutter speed is 250

    command = [f"gphoto2 --capture-image-and-download --filename={capture_directory}"] # Example of writing gphoto2 commands in Python as subprocess: https://forums.raspberrypi.com/viewtopic.php?t=271901
