# Number Analyzer

# This program collects 20 numbers from the user, calculates various statistics,
# and displays the smallest, largest, total sum, and average of the numbers.

def get_numbers():
    num_list = []
    num_index = 0

    print("Enter 20 numbers.")
    while num_index < 20:
        try:
            num = float(input(f"Enter #{num_index + 1}: "))  # User input for 20 numbers
            num_list.append(num)  # Add number to the list
            num_index += 1  # Increment the loop iteration count
        except ValueError:
            print("Invalid input. Please enter a valid numerical value.")

    return num_list

def calculate_statistics(numbers):
    total_numbers = sum(numbers)  # Calculate the total sum of numbers
    max_num = max(numbers)  # Calculate the maximum number
    min_num = min(numbers)  # Calculate the minimum number
    avg = total_numbers / len(numbers)  # Calculate the average

    return total_numbers, max_num, min_num, avg

def display_results(total, max_num, min_num, avg):
    print(f"The smallest number in the list is {min_num}.")
    print(f"The largest number in the list is {max_num}.")
    print(f"The total sum of all numbers in the list is {total}.")
    print(f"The average of all numbers in the list is {avg}.")

def main():
    numbers = get_numbers()  # Get 20 numbers from the user
    total, max_num, min_num, avg = calculate_statistics(numbers)  # Calculate statistics
    display_results(total, max_num, min_num, avg)  # Display results

if __name__ == '__main__':
    main()

