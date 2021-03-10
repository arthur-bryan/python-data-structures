from stack import Stack

palavra = input("Informe a palavra: ")

def is_palindrome(word):
	result = True
	inverse_word = Stack()
	for letter in range(len(word), 0, -1):
		inverse_word.push(word[letter-1])
	for letter in range(len(word)):
		if word[letter] != inverse_word.data[letter]:
			result = False
	return result

print(is_palindrome(palavra))
