# Hot Dog Cookout Planner
# This program calculates the number of hot dog and bun packages needed for a cookout based on guest count and hot dogs per guest.

import math

def calculate_cookout_requirements():
    while True:
        try:
            # Ask user for the number of total guests attending
            guests = int(input('How many people will attend the cookout? '))

            # Ask user for the number of hot dogs each guest will have
            hdperguest = int(input('How many hot dogs will each guest have? '))

            # Calculate total number of hot dogs needed
            totalhd = guests * hdperguest

            # Calculate packages of hotdogs needed
            packagehd = math.ceil(totalhd / 10)

            # Calculate packages of buns needed
            packagebun = math.ceil(totalhd / 8)

            # Calculate number of hotdogs left over
            leftoverhd = packagehd * 10 - totalhd

            # Calculate number of buns left over
            leftoverbun = packagebun * 8 - totalhd

            # Display the results
            print("Minimum number of hot dog packages required: " + str(packagehd))
            print("Minimum number of bun packages required: " + str(packagebun))
            print("Left over hot dogs: " + str(leftoverhd))
            print("Left over buns: " + str(leftoverbun))
            break  # Exit the loop if all inputs are valid
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    while True:
        calculate_cookout_requirements()
        another_cookout = input("Do you want to plan another cookout? (yes/no): ").lower()
        if another_cookout.lower() != "yes" and another_cookout.lower() != "y":
            print("Exiting the cookout planner.")
            break

if __name__ == "__main__":
    main()

