import subprocess

summary_command = ["gphoto2",
                   "--auto-detect"
                   ]

subprocess.run(summary_command)

def capture(camera: str):
    if camera == "nikond3500":
        model = "Nikon DSC 3500"
        port = "usb:001, 011"
    elif camera == "nikond70":
        model = "Nikon DSC D70 (PTP mode)"
        port = "usb:001, 010"


    command = ["gphoto2",
               "--camera",
               model,
               "--port",
               port,
               "--capture-image-and-download",
               "--no-keep"]
    
    subprocess.run(command)
    
if __name__ == "__main__":
    capture("nikond3500")
    capture("nikond70")