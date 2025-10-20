capture_directory = r"C:\Users\hacks\Documents\eng810\diyscanner\capture_dir"  # this sets the directory that each captured image will be written to; the path for this will change depending on the machine where the program is being run

# These settings are set outside of the capture.py script for now in anticipation that I might change them later
# Setting this up as a dictionary makes it easier to call all of the settings into the capture.py script with one import line
capture_settings = {
    "ISO": 200,
    "aperture": 900,
    "shutter_speed": 250,
    "num_captures": 1
}