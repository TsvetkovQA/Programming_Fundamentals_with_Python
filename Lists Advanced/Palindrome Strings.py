words = input().split()
palindrome = input()

found_palindromes = [word for word in words if word == word[::-1]]
count = found_palindromes.count(palindrome)

print(found_palindromes)
print(f"Found palindrome {count} times")
