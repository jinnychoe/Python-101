# Ticket Sales Calculator

# This program calculates the total income generated from ticket sales for three different classes.

# Global Constants
PRICE_CLASS_A = 20
PRICE_CLASS_B = 15
PRICE_CLASS_C = 10

# This program calculates the total income generated from ticket sales for three different classes.

def get_seats(class_name):
    while True:
        try:
            seats = int(input(f"Input the total number of seats sold for {class_name} seats: "))
            if seats < 0:
                raise ValueError("Number of seats sold must be a non-negative integer.")
            return seats
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_income(seats, ticket_price):
    income = seats * ticket_price  # Calculate income from seats
    return income

def calculate_total_income(class_a_seats, class_b_seats, class_c_seats):
    total_income = (
        calculate_income(class_a_seats, PRICE_CLASS_A)
        + calculate_income(class_b_seats, PRICE_CLASS_B)
        + calculate_income(class_c_seats, PRICE_CLASS_C)
    )
    return total_income

def main():
    print(f"Ticket Prices: \nClass A - ${PRICE_CLASS_A} \nClass B - ${PRICE_CLASS_B} \nClass C - ${PRICE_CLASS_C}\n")
    
    while True:
        class_a_seats = get_seats("Class A")
        class_b_seats = get_seats("Class B")
        class_c_seats = get_seats("Class C")
        total_income = calculate_total_income(class_a_seats, class_b_seats, class_c_seats)
        print(f"The total income generated from ticket sales is: ${total_income:.2f}")
        
        another_calculation = input("Do you want to calculate income for another set of ticket sales? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Exiting the ticket sales income calculator.")
            break

if __name__ == '__main__':
    main()

