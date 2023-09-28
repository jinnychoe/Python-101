# Test Score Analyzer

# This program collects a series of test scores from the user, calculates the total score,
# and computes the average score. It then stores the scores and results in a file.

def get_scores():
    # Create an empty list to store test scores.
    test_scores = []

    # Create a variable to control the loop.
    again = 'y'

    # Get test scores from the user and add them to the list.
    while again == 'y':
        try:
            # Get a test score and add it to the list.
            value = float(input('Enter a test score: '))
            test_scores.append(value)

            # Check if the user wants to add another score.
            print('Do you want to add another score?')
            again = input('Enter "y" for yes, or anything else for no: ')
            print()
        except ValueError:
            print('Invalid input. Please enter a valid numerical score.')

    # Return the list of test scores.
    return test_scores

def get_total(value_list):
    # Initialize a variable to use as an accumulator.
    total = 0.0

    # Calculate the total of the list elements.
    for num in value_list:
        total += num

    # Return the total.
    return total

def main():
    scores = get_scores()  # Calls the get_scores function to collect test scores.

    total_scores = get_total(scores)  # Calculates the sum of test scores.

    # Calculate the average score.
    average_score = total_scores / len(scores)

    # Print the results.
    print('Scores:', scores)
    print('Total scores:', total_scores)
    print('Average:', average_score)

    # Write the results to a file.
    with open("scorefile.txt", 'w') as scorefile:
        scorefile.write('Scores: ' + str(scores) + '\n')
        scorefile.write('Total: ' + str(total_scores) + '\n')
        scorefile.write('Average: ' + str(average_score) + '\n')

# Call the main function.
if __name__ == '__main__':
    main()

