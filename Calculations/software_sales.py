# Software Sales Calculator
# This program calculates the total cost of software packages based on quantity and applies a discount.

def calculate_total_cost(quantity):
    # Retail price per package
    retail = 99

    # Determines the discount value based on the quantity purchased
    if quantity < 10:
        discount = 0
    elif quantity >= 10 and quantity <= 19:
        discount = 10
    elif quantity >= 20 and quantity <= 49:
        discount = 20
    elif quantity >= 50 and quantity <= 99:
        discount = 30
    elif quantity >= 100:
        discount = 40
    else:
        print('Invalid input. Quantity must be a positive integer.')

    if quantity > 0:
        # Calculates the amount of discount based on the quantity purchased
        amountdiscount = (discount / 100) * (quantity * retail)

        # Calculates the total cost after applying the discount
        total = (quantity * retail) - amountdiscount

        # Display the discount and total cost
        print('Discount: ' + str(discount) + '%')
        print('Total after discount: $' + str(total))

def main():
    while True:
        try:
            # User inputs the number of packages purchased
            quantity = int(input('Input the number of packages (or enter 0 to exit): '))

            if quantity == 0:
                print('Exiting the program.')
                break

            if quantity < 0:
                print('Invalid input. Quantity must be a positive integer.')
                continue  # Continue the loop to ask for input again

            calculate_total_cost(quantity)
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

if __name__ == "__main__":
    main()

