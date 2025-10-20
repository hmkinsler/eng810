# Write your solution here
def even_numbers(my_list):
    new_list = []

    for i in my_list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list

if __name__ == "__main__":
    my_list = [1, -2, 3, -4, 5]
    result = even_numbers(my_list)
    print(f"original {my_list}")
    print(f"new {new_list}")