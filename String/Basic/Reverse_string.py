def reverseString(word):
    i = len(word) - 1
    j = len(word) - 1
    newword = ""

    while i >= 0:
        if word[i] != ' ':
            i -= 1
        else:
            newword += word[i + 1:j + 1]
            newword += ' '
            i -= 1
            j = i

    newword += word[0:j + 1]

    return newword


if __name__ == "__main__":
    word = input("Enter a string: ")
    print(reverseString(word))