# Write your solution here
x = [1, 2, 3, 4, 5]
index = 0 

while True:
    index = int(input("Index: "))

    if index != -1:
        y = int(input("New value: "))
        x[index] = y
        print(x)

    else: break