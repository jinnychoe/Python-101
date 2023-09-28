# Caesar Cipher

# This program takes a sentence as input, tokenizes it into words, and applies a Caesar cipher transformation to each word.
# It then prints the transformed sentence.

# Get a sentence as input from the user.
def str_input():

    while True:
        user_input = input("Type a sentence: ")
        return user_input

# Tokenize the sentence by splitting it into words.
def tokenize(string):

    tokens = string.split(" ")
    token_list = []
    for word in tokens:
        token_list.append(word)
    return token_list

# Apply a Caesar cipher transformation to a string.
def cipher(string):

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_shift_13 = alphabet[13:] + alphabet[:13]
    caesar_string = ''
    for letter in string.upper():
        if letter in alphabet:
            index = alphabet.index(letter)
            caesar_string += alphabet_shift_13[index]
        else:
            caesar_string += letter
    return caesar_string

# Main function to apply Caesar cipher to a sentence.
def main():

    an_input = str_input()
    string_token = tokenize(an_input)
    shifted_words = [cipher(word) for word in string_token]
    output_string = " ".join(shifted_words)

    print(f"The output is {output_string}")

if __name__ == '__main__':
    main()

