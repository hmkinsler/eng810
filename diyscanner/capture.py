# To be able to control my DSLR cameras on the Raspberry Pi, I followed this tutorial for installing libgphoto and gphoto2: https://pimylifeup.com/raspberry-pi-dslr-camera-control/

# I referred to this resource to understand how to write Python scripts that call gphoto2 commands: https://pypi.org/project/gphoto2/

import os # this library will allow me to write files to my machine
import gphoto2 as gp # since I have used gphoto2 from the Raspberry Pi terminal, I should be able to use python-gphoto2 as a interface for using it within my Python scripts
# https://github.com/jim-easterbrook/python-gphoto2
from settings import capture_directory # this ensures that I can easily change the directory that I want to write photos to across different machines
from settings import capture_settings # brings in default values for ISO, aperture, shutter speed, and number of captures

def capture_page(camera):
    # I am unsure about if this is the best way to do it, but I'm trying to have all settings that would be changed variably in just the settings.py script, so I'm going to call them here so I can write them into the capture function
    iso = capture_settings["ISO"]
    aperture = capture_settings["aperture"]
    shutter_speed = capture_settings["shutter_speed"]
    num_captures = capture_settings["num_captures"]
    
    # Check that a directory is available for saving captured images to -- based off this script: https://djangocentral.com/check-if-a-directory-exists-if-not-create-it/
    if os.path.isdir(capture_directory): # Checks that the directory defined in settings.py exists
        print("Capture directory exists")
    else:
        os.makedirs(capture_dir) # If capture directory does not exist, one is created before any images are captured
        print("Capture directory has been created")

    # Check what type of capture is being requested and take photos based on how many were set with num_captures variable, using either the left camera, the right camera, or capturing images with both cameras at once
    for i in range num_captures:
        if camera == "both":
            left_camera = gp.camera() # I need to figure out how to distinguish between the two cameras in the way gphoto2 requires
            right_camera = gp.camera()
        
            # Commands for capturing image based off this script: https://github.com/jim-easterbrook/python-gphoto2/blob/main/examples/capture-image.py
            left_camera.init()
            print("Image capturing for left camera")
            left_camera.capture(gp.GP_CAPTURE_IMAGE) # I think this is mostly based on gphoto2's commands as they are written for terminal, so this would capture the image temporarily on the camera
            left_camera.file_get()
            left_camera.save(capture_directory) # The intention here is to save the image to the capture directory -- are there going to be issues with file names and potentially overwriting the file?

            # Now I basically repeat these steps for the other camera -- I do think I'd want to improve the ordering of this so that the images capture closer in time together, but I'm also unsure as to what problems might be encountered if the temporary file on one camera gets lost while the other camera is capturing an image -- need to better understand how gphoto2 functions to solve this

            right_camera.init()
            print("Image capturing for right camera")
            right_camera.capture(gp.GP_CAPTURE_IMAGE) 
            right_camera.file_get()
            right_camera.save(capture_directory)

        elif camera == "left":
            left_camera = gp.camera()
            left_camera.init()
            print("Image capturing for left camera")
            left_camera.capture(gp.GP_CAPTURE_IMAGE) 
            left_camera.file_get()
            left_camera.save(capture_directory) 
        
        else: # Assumes that if we're not using the left camera only or both cameras that we're working with the right camera
            right_camera.init()
            print("Image capturing for right camera")
            right_camera.capture(gp.GP_CAPTURE_IMAGE) 
            right_camera.file_get()
            right_camera.save(capture_directory)