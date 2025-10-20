# Write your solution here
x = 0 

while x != "visual studio code": 
    x = input("Editor: ")
    x = x.lower() # Ensure x is lowercase
    
    if x == "word" or x == "notepad":
        print("awful")

    elif x == "visual studio code":
        print("an excellent choice!")

    else:
        print("not good")

