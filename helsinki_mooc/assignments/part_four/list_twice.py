# Write your solution here
list = []

while True:
    x = int(input("New item: "))

    if x == 0:
        break

    else:
        list.append(x)
        sorted_list = sorted(list)

        print(f"The list now: {list}")
        print(f"The list in order: {sorted_list}")

print("Bye!")