# Write your solution here
def list_sum(a, b):
    sums = []
    index = 0

    for i in a:
        x = a[index] + b[index]
        index += 1
        sums.append(x)

    return sums

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b))