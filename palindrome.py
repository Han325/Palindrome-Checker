word = input("Please enter a word: ")

for i in range(len(word)):
    if word[i] != word[-i-1]:
        print("No, this word is not a palindrome.")
        break
else:
    print('Yes, this word is palindrome.')

