# Write your solution here
amount = int(input("How many items: "))
x = 1
items = []

while amount > 0:
    y = int(input(f"Item {x}: "))
    items.append(y)
    amount -= 1
    x += 1

print(items)