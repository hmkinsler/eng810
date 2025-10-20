
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

def triangle(size):
    # You should call function line here with proper parameters
    x = size
    y = 0

    while y <= x:
        line(y, "#")
        y += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
