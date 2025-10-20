# Write your solution here
def same_chars(char: str, x: int, y: int):
    if y > (len(char)-1) or x > (len(char)-1):
        return False
    elif char[x] == char[y]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))