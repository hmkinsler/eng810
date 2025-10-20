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

def box_of_hashes(height):
    # You should call function line here with proper parameters
    while height > 0:
        line(10, "#")
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
