# Write your solution here
x = []
y = 1
print(f"The list is now {x}")

while True:
    method = input("a(d)d, (r)emove or e(x)it: ")

    if method == "d":
        x.append(y)
        y += 1
        
        print(f"The list is now {x}")
    
    elif method == "r":
        y -= 1
        x.remove(y)

        print(f"The list is now {x}")

    elif method == "x":
        break

print("Bye!")
