secret_mesages = input().split()
new_mesages = []
for word in secret_mesages:
    digit , let = "", ""
    for letter in word:
        if letter.isdigit():
            digit += letter
        else:
            let += letter

    letter_for_digit = chr(int(digit))
    if len(let) != 1:
        new_word = f"{let[-1]}{let[1:-1]}{let[0]}"
    else:
        new_word = let
    new_word = letter_for_digit + new_word
    new_mesages.append(new_word)
print(*new_mesages)


    
