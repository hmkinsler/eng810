# Copy here code of line function from previous exercise
def line(num : int, x : str):
    count = 0
    
    while count < num:
        if x == "":
            x = "*"
            count += 1
        else:
            count += 1

    print(count * x[0])

def square(size, character):
    # You should call function line here with proper parameters
    x = size
    y = character

    while size > 0:
        line(x, y)
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")