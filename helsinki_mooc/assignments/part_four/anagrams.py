# Write your solution here
def anagrams(x: str, y: str):
    x_sorted = sorted(x)
    y_sorted = sorted(y)
    
    if x_sorted == y_sorted:
        return True
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))