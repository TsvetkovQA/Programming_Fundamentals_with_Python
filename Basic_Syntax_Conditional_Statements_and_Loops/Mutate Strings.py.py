string1 = input()
string2 = input()
last_string = string1
for character_index in range(len(string1)):
    left_part = string2[0:character_index+1]
    right_part = string1[character_index+1:]
    new_string = left_part + right_part
    if new_string != last_string:
        print(new_string)
        last_string = new_string
        
