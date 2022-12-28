if __name__ == '__main__':
    chars = input()
    dct = {}
    for char in chars:
        dct[char] = dct.get(char, 0) + 1

    word = input()
    for char in word:
        if char in dct:
            dct[char] -= 1
            if dct[char] == 0:
                del dct[char]
        else:
            print("No")
            break
    else:
        print("Ok")
