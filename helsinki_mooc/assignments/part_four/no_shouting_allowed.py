# Write your solution here
def no_shouting(my_list):
    pruned_list = []

    for i in my_list:
        if i.isupper() == False:
            pruned_list.append(i)

    return pruned_list

if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)