# Vowel and Consonant Counter
# This program takes user input for a word and calculates the number of vowels and consonants in that word.

def str_input():
    while True:
        user_input = input("Type in one word (or 'q' to quit): ")  # User input for a word
        if user_input.lower() == 'q':
            return None  # Exit the loop if the user wants to quit
        elif user_input.isalpha():  # Checks if input contains only alphabetical characters
            return user_input
        else:
            print("Type in only alpha characters")  # If there are non-alphabetical characters, ask for input again

def count_vowels(string):
    count = 0  # Initializes the vowel counter
    for char in string:  # Checks each character in the string to see if it's a vowel
        if char.lower() in "aeiou":
            count += 1  # If the character is a vowel, add to the vowel counter
    return count  # Returns the count of vowels

def count_cons(string):
    count = 0  # Initializes the consonant counter
    for char in string:  # Checks each character in the string to see if it's a consonant
        if char.lower() not in "aeiou":
            count += 1  # If the character is a consonant, add to the consonant counter
    return count  # Returns the count of consonants

def main():
    while True:
        an_input = str_input()
        if an_input is None:
            print("Exiting the program.")
            break
        num_vowels = count_vowels(an_input)
        num_cons = count_cons(an_input)
        print(f"The number of vowels: {num_vowels}")
        print(f"The number of consonants: {num_cons}")

if __name__ == '__main__':
    main()

