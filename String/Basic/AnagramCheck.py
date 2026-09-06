def CheckAnagrams(str1, str2):
    if len(str1) != len(str2):
        return False
    freq = [0] * 26
    for char in str1:
        freq[ord(char) - ord('A')] += 1

    for char in str2:
        freq[ord(char) - ord('A')] -= 1

    for count in freq:
        if count != 0:
            return False
    return True 

if __name__ == "__main__":
    Str1 = "INTEGER"
    Str2 = "TEGERNI"

    if CheckAnagrams(Str1, Str2):
        print("True")
    else:
        print("False")
