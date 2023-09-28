# Property Tax Calculator

# This program calculates the assessed value and property tax based on the actual value of a property.

ASSESSMENT_RATE = 0.6  # 60% assessment rate
TAX_RATE = 0.72  # $0.72 per $1 assessed value

def get_actual_value():
    while True:
        try:
            act_value = float(input("Input the actual value of the property: $"))
            if act_value < 0:
                raise ValueError("Actual value must be a non-negative number.")
            return act_value
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_assessed_value(act_value):
    assessed_value = act_value * ASSESSMENT_RATE  # Calculate assessed value
    return assessed_value

def calculate_property_tax(assessed_value):
    property_tax = assessed_value * TAX_RATE  # Calculate property tax
    return property_tax

def main():
    while True:
        act_value = get_actual_value()  # Get the actual value of the property
        assessed_value = calculate_assessed_value(act_value)
        property_tax = calculate_property_tax(assessed_value)
        print(f"\nAssessment Rate: {ASSESSMENT_RATE * 100}%")
        print(f"Tax Rate: {TAX_RATE * 100}%")        
        print(f"\nThe actual value of the property is ${act_value:.2f}")
        print(f"The assessed value of the property is ${assessed_value:.2f}")
        print(f"The property tax of the property is ${property_tax:.2f}")

        
        another_property = input("Do you want to calculate the property tax for another property? (yes/no): ").lower()
        if another_property != "yes":
            print("Exiting the property tax calculator.")
            break

if __name__ == '__main__':
    main()

