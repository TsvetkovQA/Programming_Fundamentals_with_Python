while True:
    string = input()
    if string == "End":
        break
    if string != "SoftUni":
        result = ''.join(char * 2 for char in string)
        print(result)
