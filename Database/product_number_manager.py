# Product and Name Manager
# This program allows you to search for a product number in a list stored in the 'product_numbers.txt' file and provides results on whether the number was found or not.

def search_product_number():
    try:
        # Attempt to open the file for reading
        with open('product_numbers.txt', 'r') as file:
            # Read the lines of the file into a list
            prodNums = [line.strip() for line in file]

        # Get user input
        search = input('Enter a product number: ')

        # Check if the input is in the list
        if search in prodNums:
            print(search, ' was found on the list.')
        else:
            print(search, ' was not found on the list.')
    except FileNotFoundError:
        print("The product_numbers.txt file does not exist.")
    except Exception as e:
        print("An error occurred:", e)


def input_and_store_product_numbers():
    # Create an empty list to store product numbers
    productNumList = []
    again = 'y'

    # Continue adding product numbers until the user decides to stop
    while again == 'y':
        product_number = input('Enter a product number: ')
        productNumList.append(product_number)  # Append product number to the list
        print()

        print('Do you want to add another product number?')
        again = input('Press "y" for Yes, or any other key for No: ')
        print()
        print('Here are the product numbers you entered:')

        # Loop through each product number in the list and print them
        for number in productNumList:
            print(number)

        # Write the product numbers to a file
        outfile = open('product_numbers.txt', 'w')
        outfile.write('\n'.join(productNumList))
        outfile.close()
        print('Recorded the product numbers in the list.')

def main():
    while True:
        print("\nMenu:")
        print("1. Search Product Number")
        print("2. Input and Store Product Numbers")
        print("3. Quit Program")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            search_product_number()
        elif choice == '2':
            input_and_store_product_numbers()
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()

