# Average Rainfall Calculator

# This program calculates the average monthly rainfall over a given number of years.
# It collects rainfall data for each month and year from the user.

def get_rainfall_data():
    # User input: Number of years
    years = int(input("Enter the total number of years: "))
    
    rainfall_data = []  # List to store rainfall data for each month

    for year in range(years):  # Outer loop for each year
        for month in range(12):  # Inner loop for each month of the year
            try:
                # User input: Inches of rainfall for a specific month and year
                rainfall = float(input(f"Enter the inches of rainfall for month {month + 1} of year {year + 1}: "))
                rainfall_data.append(rainfall)  # Add rainfall input to the list
            except ValueError:
                print("Invalid input. Please enter a valid numerical value.")

    return rainfall_data

def calculate_statistics(rainfall_data):
    total_rainfall = sum(rainfall_data)  # Calculate the total rainfall
    total_months = len(rainfall_data)  # Calculate the total number of months
    average_rainfall = total_rainfall / total_months  # Calculate the average rainfall per month

    return total_months, total_rainfall, average_rainfall

def display_results(total_months, total_rainfall, average_rainfall):
    print(f"Total number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average inches of rainfall per month: {average_rainfall:.2f}")

def main():
    rainfall_data = get_rainfall_data()  # Get rainfall data from the user
    total_months, total_rainfall, average_rainfall = calculate_statistics(rainfall_data)  # Calculate statistics
    display_results(total_months, total_rainfall, average_rainfall)  # Display results

if __name__ == '__main__':
    main()

