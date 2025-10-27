---
title: Week Ten Documentation Notes
course: ENG 810
semester: Fall 2025
tags: #documentation
created: 2025-10-19
---

## Current Status of DIY Scanner Backend Files
- Further reworking of the [capture.py](/diyscanner/capture.py) script to work on successfully capturing images for both of my Nikon cameras with the [gphoto2 command line utility](http://www.gphoto.org/doc/manual/ref-gphoto2-cli.html#cli-examples) on the Raspberry Pi

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
- [Assignments](/helsinki_mooc/assignments/part_four/) are a WIP; currently at 78% completion
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
- I was able to get images captured on the two cameras separately and am able to more consistently take photos using [capture.py](/diyscanner/capture.py) with the Nikon D70, but I am still working on a way to more consistently identify the two cameras apart from the --port command because the port ID changes for the cameras each time that they are plugged into the Raspberry Pi or turned off/on
- In order to see if there are pre-existing tools, softwares, or scripts that are used for scanning, I tried installing the dependencies for [Spreads](https://spreads.readthedocs.io/en/v0.4.2/) and (seemed to) confirm that it is too outdated to be usable on Linux or other Raspberry Pi operating systems
- I ran into similar issues testing out [Scantailor](https://scantailor.org/), though this may be worth [reapproaching with a Windows machine](https://www.youtube.com/watch?v=IM1EqJ3MCII) based on some recent video tutorials I came across or seeing if a [more recent build with some updated dependencies](https://github.com/4lex4/scantailor-advanced) works better

# Experimenting w/ Arduino to control foot pedal
- Still need to draw up wire diagram
- Plan to revisit the [capture.py](/diyscanner/capture.py) script to use either buttons or foot pedal switches to determine which camera(s) are included in the main function block