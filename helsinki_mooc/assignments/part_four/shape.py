# Copy here code of line function from previous exercise and use it in your solution
def line(num : int, x : str):
    count = 0
    
    while count < num:
        if x == "":
            x = "*"
            count += 1
        else:
            count += 1

    print(count * x[0])

def shape(size: int, char_1: str, rows: int, char_2: str):
    x = size
    y = 0

    while y <= x:
        line(y, char_1)
        y += 1
    
    while rows > 0:
        line((y - 1), char_2)
        rows -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")