# Sales Tax Calculator

# This program calculates state and county sales tax based on total sales for the month.

COUNTY_TAX_RATE = 0.025
STATE_TAX_RATE = 0.05

# This program calculates state and county sales tax based on total sales for the month.

def get_total_sales():
    while True:
        try:
            total_sales = float(input("Please input the total sales for the month: $"))
            if total_sales < 0:
                raise ValueError("Total sales must be a positive number.")
            return total_sales
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_county_sales_tax(total_sales):
    county_tax = total_sales * COUNTY_TAX_RATE
    return county_tax

def calculate_state_sales_tax(total_sales):
    state_tax = total_sales * STATE_TAX_RATE
    return state_tax

def calculate_total_sales_tax(county_tax, state_tax):
    total_tax = county_tax + state_tax
    return total_tax

def main():
    print(f"County Sales Tax Rate: {COUNTY_TAX_RATE * 100}%")
    print(f"State Sales Tax Rate: {STATE_TAX_RATE * 100}%")
    
    while True:
        total_sales = get_total_sales()
        county_tax = calculate_county_sales_tax(total_sales)
        state_tax = calculate_state_sales_tax(total_sales)
        total_tax = calculate_total_sales_tax(county_tax, state_tax)
        print(f"\nThe total sales for the month is: ${total_sales:.2f}")
        print(f"The state sales tax for the month is: ${state_tax:.2f}")
        print(f"The county sales tax for the month is: ${county_tax:.2f}")
        print(f"The total sales tax for the month is: ${total_tax:.2f}\n")
        
        another_calculation = input("Do you want to calculate sales tax for another month? (yes/no): ").lower()
        if another_calculation != "yes":
            print("Exiting the sales tax calculator.")
            break

if __name__ == '__main__':
    main()

