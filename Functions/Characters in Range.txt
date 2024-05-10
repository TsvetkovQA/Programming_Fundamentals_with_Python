def characters_in_between(char1, char2):
    start_ascii = ord(char1)
    end_ascii = ord(char2)

    result = ""

    for ascii_code in range(start_ascii + 1, end_ascii):
        result += chr(ascii_code) + " "

    return result.strip()



char1 = input()
char2 = input()


result = characters_in_between(char1, char2)


print(result)
