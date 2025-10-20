# Write your solution here
def distinct_numbers(my_list):
    unique = []

    for i in my_list:
        if i not in unique:
            unique.append(i)

    unique.sort()

    return unique

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))