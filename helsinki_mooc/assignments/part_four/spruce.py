# Write your solution here
def line(w: int, x: int):
    print((w * " ") + (x * "*") + "*" + (x * "*") + (w * " "))

def spruce(size):
    print("a spruce!")
    
    width = size - 1
    star = 0

    while size > 0:
        line(width, star)
        size -= 1
        width -= 1
        star += 1

    trunk_sides = star - 1
    print((trunk_sides * " ") + "*" + (trunk_sides * " "))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)