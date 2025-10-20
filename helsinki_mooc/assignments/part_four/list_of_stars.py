# Write your solution here
def list_of_stars(my_list):
    for i in my_list:
        print(i * "*")

# Function block
if __name__ == "__main__":
    my_list = [3, 7, 1, 1, 2]
    list_of_stars(my_list)