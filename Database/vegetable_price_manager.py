# Vegetable Price Manager

# This program allows users to manage a list of vegetables and their prices.
# Users can list all vegetables, add new vegetables, change the price of existing vegetables,
# delete existing vegetables, and save the data to a file.

import pickle

# Load vegetable data from a file or create an empty dictionary if the file is not found.
def load_vegetables():

    try:
        with open('vegetables.dat', 'rb') as file:
            return pickle.load(file)
    except FileNotFoundError:
        return {}

# Save the vegetable data to a file.
def save_vegetables(vegetables):
    with open('vegetables.dat', 'wb') as file:
        pickle.dump(vegetables, file)

# List all vegetables and their prices.
def list_vegetables(vegetables):

    if vegetables:
        print('Price of vegetables:')
        for item, price in vegetables.items():
            print(f'{item}\t\t${price:.2f}')
    else:
        print('You have not added any vegetables to the file!\n')

# Add a new vegetable and its price to the list.
def add_vegetable(vegetables):

    while True:
        item = input('Enter vegetable name: ')
        while not item:
            print("Please enter a vegetable name: ")
            item = input('Enter vegetable name: ')
        if item == "":
            break
        try:
            price = float(input('Please input the price of the vegetable: $ '))
            vegetables[item] = price
            break
        except ValueError:
            print("Invalid price.\n")

    print(f'{item} has been added to the list.\n')

# Change the price of an existing vegetable.
def change_price(vegetables):

    item = input('Enter the name of the vegetable to change: ')
    if item in vegetables:
        try:
            price = float(input('Enter the price of the vegetable: $'))
            vegetables[item] = price
            print(f'The price of {item} has been changed to ${price:.2f}.\n')
        except ValueError:
            print("Invalid price.\n")
    else:
        print(f'{item} not found on the list.\n')

# Delete an existing vegetable from the list.
def delete_vegetable(vegetables):

    if not vegetables:
        print("No vegetables in vegetables.dat.\n")
        return
    item = input('Enter the name of the vegetable to delete: ')
    if item in vegetables:
        del vegetables[item]
        print(f'{item} deleted.\n')
    else:
        print(f'{item} cannot be found on the list.\n')

# Main function to manage vegetable data.
def main():

    vegetables = load_vegetables()
    
    while True:
        print('Vegetables and prices')
        print('1: List all vegetables')
        print('2: Add new vegetable')
        print('3: Change price of existing vegetable')
        print('4: Delete existing vegetable')
        print('5: Save and Quit')
        num = input('Enter a number: ')

        if num == '1':
            list_vegetables(vegetables)
        elif num == '2':
            add_vegetable(vegetables)
        elif num == '3':
            change_price(vegetables)
        elif num == '4':
            delete_vegetable(vegetables)
        elif num == '5':
            save_vegetables(vegetables)
            print('Saving to vegetables.dat and quitting the program.\n')
            break
        else:
            print('Please choose 1, 2, 3, 4, or 5.\n')

if __name__ == '__main__':
    main()

