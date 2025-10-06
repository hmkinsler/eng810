---
title: Week Eight Documentation Notes
course: ENG 810
semester: Fall 2025
tags: #documentation
created: 2025-10-06
---
# Organizing directory & DIY Scanner files
- I moved all of the ENG 810 documentation and files to its own repository so that they are separate from the files and previous development projects that I have worked on for the [DIY Scanner software](https://github.com/hmkinsler/diyscanner)
- Added guidance on how to navigate repository to the [README file](README.md)
- I did get the current version of the DIY Scanner software working on my Windows machine, and can write up documentation for how to launch the software GUI if requested

## Current Status of DIY Scanner Backend Files
This would include all of the files in /scanning and some from /utils
### Files that work and I know why
- [main.py](https://github.com/hmkinsler/diyscanner/blob/main/scanning/main.py)
    - This script mostly sets up the modularity for the rest of the scanning backend files
- [set_directories.py](https://github.com/hmkinsler/diyscanner/blob/main/utils/set_directories.py)
    - Helper script that checks whether or not there are directory locations for saving images when they are first captured, processed, and then compiled into a PDF file
- [settings.py](https://github.com/hmkinsler/diyscanner/blob/main/utils/settings.py)
    - This script sets the default values for different setting variables for each stage of the scanning workflow, such as setting camera ISO to a default value of 100 or the number of images to be captured to 1

### Files that work and I don't know why
- [capture.py](https://github.com/hmkinsler/diyscanner/blob/main/scanning/src/capture.py)
- [processing.py](https://github.com/hmkinsler/diyscanner/blob/main/scanning/src/processing.py)
    - For this file, I mostly am focused on process_images(), the detect_page() function is not currently working because it's related to a machine learning task I was working on previously training a YOLOv5 model to detect the boundaries for the left and right pages of a book to conduct automatic cropping. That part of the script is entirely a WIP for now.
### Files that don't work and I know why
### Files that don't work and I don't know why
### Files that are still a WIP, may need to be scrapped, or I don't know if they work
- [metadata.py](https://github.com/hmkinsler/diyscanner/blob/main/scanning/src/metadata.py)
- [pdf_generator.py](https://github.com/hmkinsler/diyscanner/blob/main/scanning/src/pdf_generator.py)

## Current Status of DIY Scanner Frontend / GUI Files
This would include all of the files in /gui and some from /utils
### Files that work and I know why
### Files that work and I don't know why
- [browse.py](https://github.com/hmkinsler/diyscanner/blob/main/utils/browse.py)
    - This is a helper script that provides a workaround to an issue with how Tkinter handles browsing of file directories
- [rename_files.py](https://github.com/hmkinsler/diyscanner/blob/main/utils/rename_files.py)
    - I generally know how this script works, I just don't fully understand the REGEX for the file naming convention
    - I don't think I generally use this script at the moment, I probably wrote it for managing file names earlier on while working on the project
- [bookscanning.py](https://github.com/hmkinsler/diyscanner/blob/main/gui/bookscanning.py)
    - The main thing I don't understand is how the class for the BookScanningApp frame works. There's some additional problems here with managing window size, and I have not easily been able to make elements resizable in the past. 
    - I am also unsure on how show_content_frame() works -- this is meant to make it so that each of the different GUI setting pages are displayed in a consistent frame when they are selected from the options menu, but I don't know exactly how it's doing that

### Files that don't work and I know why
### Files that don't work and I don't know why
### Files that are still a WIP, may need to be scrapped, or I don't know if they work
- Specific option pages
    - [capture_gui.py](https://github.com/hmkinsler/diyscanner/blob/main/gui/src/capture_gui.py)
    - [pdf_gui.py](https://github.com/hmkinsler/diyscanner/blob/main/gui/src/pdf_gui.py)
    - [preview_gui.py](https://github.com/hmkinsler/diyscanner/blob/main/gui/src/preview_gui.py)
    - [processing_gui.py](https://github.com/hmkinsler/diyscanner/blob/main/gui/src/processing_gui.py)
        - The main issue with all of these files is that I don't understand how classes work
        - Many of them are WIPs as well since the back-end is not fully developed, and I've been fiddling around with how I want the GUI to be designed in terms of the UI
        - There's also a subprocess within several of these scripts that I use to capture preview images with the camera and test them out

# Helsinki MOOC
## Unit One Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/written_notes/part_one.md)
- Finished assignments with 96% as final grade for [unit assignments](/helsinki_mooc/assignments/part_one/)
## Unit Two Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_two.py)
- Finished assignments with 100% as final grade for [unit assignments](/helsinki_mooc/assignments/part_two/)
## Unit Three Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_three.py)
- [Assignments](/helsinki_mooc/assignments/part_three/) are a WIP; currently at 91% completion
## Unit Four Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_four.py)
- Not yet started assignments
- Set-up VS Code IDE with [extension for MOOC assignment grading](https://www.mooc.fi/en/installation/vscode/)

# ENG 810 / CRD 704 Pilot Study
- Got approval from Dr. Beare to work on pilot study for his course that is focused on the DIY Scanner software


# Raspberry Pi
- Successfuly was able to [take a picture and save the file to a directory on the Raspberry Pi](https://youtu.be/PDsRIjVdeC0) using [this tutorial](https://pimylifeup.com/raspberry-pi-dslr-camera-control/) for controlling DSLRs on Raspberry Pi with [gphoto2](http://www.gphoto.org/)


# Experimenting w/ Arduino to control foot pedal
- Succesfully determined that the transcription foot pedal wires are analog using multimeter
- Wrote several Arduino scripts to test development of basic circuits
    - Example of [lighting up LED at one second intervals for duration of one second](https://youtu.be/UqPB7h-baT8)
    - Example of [lighting up LED while button is pressed](https://youtu.be/Z7h4gAJb_Q8)
    - Example of [turning LED on and off each time button is pressed](https://youtu.be/Km_k3divVW8)
- Unsuccessfully attempted to use [foot pedal as an analog input](images\foot_pedal_circuit_attempt.jpg) that can turn the LED on and off; will likely need to follow-up with Dr. Rieder to debug