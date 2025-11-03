# Followed tutorial on projects.raspberrypi.org/en/projects/physical-computing/7 to set up buttons to fire cameras
from gpiozero import Button
import subprocess

summary_command = ["gphoto2",
                   "--auto-detect"
                   ]

subprocess.run(summary_command)

def capture_nikond3500(camera: str):
    model = "Nikon DSC 3500"
    port = "usb:001, 011" # It would be helpful to return the ports based on how they're listed through the auto-detect command
    file_name = "/home/hmkinsle/Pictures/shot_%Y-%m-%d %H:%M:%S"

    command = ["gphoto2",
               "--camera",
               model,
               "--port",
               port,
               "--capture-image-and-download",
               f"filename={file_name}",
               "--no-keep"]
    
    subprocess.run(command)
def capture_nikond70():
    model = "Nikon DSC D70 (PTP mode)"
    port = "usb:001, 010"

    file_name = "/home/hmkinsle/Pictures/shot_%Y-%m-%d %H:%M:%S"

    command = ["gphoto2",
               "--camera",
               model,
               "--port",
               port,
               "--capture-image-and-download",
               f"filename={file_name}",
               "--no-keep"]
    
    subprocess.run(command)
    
d3500_button = Button(2) # Button input on GPIO2
d70_button = Button(3) # Button input on GPIO3

# Adapted from gpiozero.readthedocs.io/en/stable/reclipes.html#button-controlled-camera
d3500_button.when_pressed = capture_nikond3500 # I'm wondering if I could have one capture function that checks which button is pressed and runs the subprocess commands appropriately
d70_button.when_pressed = capture_nikond70