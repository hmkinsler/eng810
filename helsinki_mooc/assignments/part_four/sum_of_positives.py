# Write your solution here
def sum_of_positives(my_list):
    result = 0

    for i in my_list:
        if i > 0:
            result += i

    return result

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = sum_of_positives(my_list)
    print(f"The result is {result}")