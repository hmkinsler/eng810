---
title: Week Fifteen Documentation Notes
course: ENG 810
semester: Fall 2025
tags: #documentation
created: 2025-12-1
---

# Helsinki MOOC
## Unit One Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/written_notes/part_one.md)
- Finished assignments with 96% as final grade for [unit assignments](/helsinki_mooc/assignments/part_one/)
- Topics covered:
    - Basic commands and the print function
    - Chronology of statements/commands
    - Data types including strings, integers, and floats
    - Variables and how to declare them
    - Operands and operators
    - String concatenation
    - If statements

## Unit Two Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_two.py)
- Finished assignments with 100% as final grade for [unit assignments](/helsinki_mooc/assignments/part_two/)
- Topics covered:
    - Basic programming terminology, including statements, blocks, expressions, functions, type, syntax, and debugging
    - Comparison operators
    - Logical operators (i.e. and / or)
    - Conditionals and nested conditionals, including if, elif, and else
    - While loops
    - Debugging with print statements

## Unit Three Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_three.py)
- Finished assignments with 91% as final grade for [unit assignments](/helsinki_mooc/assignments/part_three/)
- Topics covered:
    - Functions and parameters
    - Loops that use conditionals
    - String operations
    - String and range methods
    - Nested loops
    - Break and continue commands

## Unit Four Progress
- Watched lecture and took [notes on concepts covered](/helsinki_mooc/py_notes/lecture_four.py)
- Finished assignments with 97% as final grade for [unit assignments](/helsinki_mooc/assignments/part_four/)
- Set-up VS Code IDE with [extension for MOOC assignment grading](https://www.mooc.fi/en/installation/vscode/)
- Topics covered:
    - How to use debugger tools such as [Python tutor](https://pythontutor.com/) or the VS Code debugger
    - How to setup VS Code as an IDE
    - Arguments and parameters in functions
    - Function return values
    - Type hints for parameters and return values
    - Lists and list methods
    - For loops

# Light Enclosure
- I am piloting a simple lighting set-up that makes use of a surge protector/extension to power the Raspberry Pi and two LED lights at the top of the scanner. I designed a [STL file for a light enclosure](F:\vscodeprojects\eng810\3d_printing\diy_scanner_light_enclosure_v1.stl) that should hold the light and power cable in place over the top of the scanner, and I then did a [test print on a 3D printer in Circuit Studio](F:\vscodeprojects\eng810\images\printing_light_enclosure_test.jpg). The test print was promising, but the dimensions for the enclosure were not correct, so a redesign and secondary test print are needed.

# Foot Pedal
- Jonathan designed a printable extension in AutoCAD that extends the current mechanism in the foot pedal to be able to connect with the push buttons that I am using for the push button circuit. These were successfully printed from the STL file he created, installed into the foot pedal, and tested to verify that they successfully are able to connect with the push buttons.
- I began putting together the foot pedal circuit, with two of the buttons ready to connect to wires that hook up to the Raspberry Pi GPIO pins. [I completed](https://youtu.be/kxHl7HsEKNw) this [Learn Soldering kit and tutorial](https://cad.onshape.com/publications/e3bdcfd963f6c27ca68a8dd5/w/d9d0b5db2dadaf990935f3dc/e/108a2a60dbb37e929885c0fd) to get familiar with basic soldering practices, and I then soldered the two buttons onto PCBs that I also tested are successfully able to connect to the Raspberry Pi.
- Now, I need to source the wires I will solder onto the two PCB boards and solder to the GPIO pin cables.

# Final Paper
- I have begun writing the final paper, with about 1500 words so far. I discussed how I might put together the paper as a webtext for publication in *Kairos* with Helen and Zach. Helen showed me how to get started creating a simple outline for the website using HTML and CSS from Bootstrap. 

# Future Steps
- Decide what to do about the current camera angle issue with the Nikon D70
- Finish setting up the foot pedal and hook it up to the Raspberry Pi
- Build the lighting module for the scanner
- Figure out how to handle the Camera Port ID issue with gphoto2-- right now the [capture.py script](/diyscanner/capture.py) is such that you have to change the ports in the script manually everytime the camera is turned on/off or (un)plugged
- Finish writing final paper