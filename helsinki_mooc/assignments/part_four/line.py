# Write your solution here
def line(num : int, x : str):
    count = 0
    
    while count < num:
        if x == "":
            x = "*"
            count += 1
        else:
            count += 1

    print(count * x[0])
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")