# Write your solution here
def all_the_longest(my_list):
    longest = ""
    result = []

    for i in my_list:
        if len(i) > len(longest):
            longest = i
    
    for i in my_list:
        if len(i) == len(longest):
            result.append(i)

    return result


if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]

    result = all_the_longest(my_list)
    print(result)