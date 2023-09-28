# Pig Latin Translator
# This program takes a sentence as input, tokenizes it into words, and translates each word into Pig Latin.
# It then prints the Pig Latin sentence.

# Get a sentence as input from the user.
def str_input():

    while True:
        user_input = input("Type a sentence: ")
        return user_input

# Tokenize the sentence by splitting it into words and converting them to uppercase.
def tokenize(string):
 
    tokens = string.split(" ")
    caps_words = []
    for word in tokens:
        caps_words.append(word.upper())
    return caps_words

# Translate each word in the list to Pig Latin.
def piglatin(string):

    pig_translation_sentence = []
    for word in string:
        translated_word = word[1:] + word[0] + "AY"
        pig_translation_sentence.append(translated_word)
    return pig_translation_sentence

def main():

    an_input = str_input()
    string_token = tokenize(an_input)
    translation = piglatin(string_token)
    output_string = " ".join(translation)
   
    print(f"The output is {output_string}")

if __name__ == '__main__':
    main()

