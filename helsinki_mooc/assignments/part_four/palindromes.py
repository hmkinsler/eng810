def palindromes(x: str):
    x_reversed = x[::-1]

    if x_reversed == x:
        palindrome = True
    else:
        palindrome = False

    return palindrome

while True:
    x = input("Please type in a palindrome: ")

    if palindromes(x) == False:
        print("that wasn't a palindrome")

    else:
        print(f"{x} is a palindrome!")
        break