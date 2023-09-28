# Vehicle Distance Calculator

# This program calculates the distance traveled by a vehicle based on its speed and travel time.

def get_speed():
    while True:
        try:
            speed = int(input("What is the speed of the vehicle in mph? "))
            if speed <= 0:
                raise ValueError("Speed must be a positive integer.")
            return speed
        except ValueError as e:
            print(f"Invalid input: {e}")

def get_hours():
    while True:
        try:
            hours = int(input("How many hours has it traveled? "))
            if hours < 0:
                raise ValueError("Hours must be a non-negative integer.")
            return hours
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_distance(speed, hours):
    distance_list = []
    for n in range(1, hours + 1):
        distance = n * speed  # Calculate distance traveled for each hour
        distance_list.append((n, distance))
    return distance_list

def display_results(distance_list):
    print("\nHour       Distance traveled")
    for hour, distance in distance_list:
        print(f"{hour}          {distance}")

def main():
    speed = get_speed()  # Get the speed of the vehicle
    hours = get_hours()  # Get the number of hours traveled
    distance_list = calculate_distance(speed, hours)  # Calculate distances
    display_results(distance_list)  # Display results

if __name__ == '__main__':
    main()

