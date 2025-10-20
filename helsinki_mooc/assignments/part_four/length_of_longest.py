# Write your solution here
def length_of_longest(my_list):
    longest = ""

    for i in my_list:
        if len(i) > len(longest):
            longest = i

    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = length_of_longest(my_list)
    print(result)