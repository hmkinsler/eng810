---
title: Week Twelve Documentation Notes
course: ENG 810
semester: Fall 2025
tags: #documentation
created: 2025-11-12
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
- [Assignments](/helsinki_mooc/assignments/part_three/) are a WIP; currently at 91% completion
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

# Raspberry Pi
- I was able to successfully [build and compile Scantailor-Advanced](/raspberry_pi/build_compile_scantailor-advanced.md)
- I successfully scanned and processed one page from a book with Scantailor, with a few caveats:
    - Scantailor is _very_ slow on the Raspberry Pi, so I might want to consider processing on a different machine after the Raspberry Pi has been used to capture all of the images. Maybe there's a way to wirelessly transmit the images from the Raspberry Pi to a Windows machine (i.e. my PC or laptop) so I can work with Scantailor there?
    - The cameras I currently have don't have lenses that are able to capture both of the scanner pages in full at their current angle, which is affecting the Nikon D70 in particular, hence why I only scanned one page/side of the book as opposed to both pages. I can either (1) purchase/use a camera lens with a different focal length, (2) opt to purchase/use different kinds of cameras (which I'm already planning to do long-term, since the Nikons are meant for my personal use), or (3) sand down the mount for the Nikon D70 enough that the angle for the camera is such that it can capture the full page with a 50mm lens.

![](/images/first_scanned_page.jpg)
![](/images/first_scanned_page_1.jpg)

# Experimenting w/ Arduino to control foot pedal
- Still need to draw up wire diagram -- I do now have access to a 3D printer at my home and in Circuit Studio, so I am considering instead designing a foot pedal with enclosures for the buttons

# Overall future steps
- Decide what to do about the current camera angle issue with the Nikon D70
- Begin making the button enclosure for the footpedal
- Build the lighting module for the scanner
- Figure out how to handle the Camera Port ID issue with gphoto2-- right now the [capture.py script](/diyscanner/capture.py) is such that you have to change the ports in the script manually everytime the camera is turned on/off or (un)plugged