import sys
import random

# Function to simulate a rolling a die with a given number of sides
def roll_die(sides):
    return random.randint(1, sides)

# Function to be able to calculate the percentage of sums that are multiples of 3
def calculate_multiple_of_three_percentage(num_rolls):
    # Roll two dice (9-sided and 9000-sided) `num_rolls` times and count multiples of 3
    multiple_of_three_count = sum(
        1 for _ in range(num_rolls) if (roll_die(9) + roll_die(9000)) % 3 == 0
    )
    # Calculate and return the percentage
    percentage = (multiple_of_three_count / num_rolls) * 100
    return percentage

# Main function to display results
def main():
    # Ensuring there is one command-line argument
    if len(sys.argv) != 2:
        print("Usage: python3 RD.py <number_of_rolls>")
        return
    
    # Validate the number of rolls
    try:
        num_rolls = int(sys.argv[1])
        if num_rolls < 1:
            raise ValueError("Number of rolls must be a positive integer.")
    except ValueError:
        print("Please provide a valid integer for the number of rolls.")
        return

    # Calculate the percentage of multiples of 3
    percentage = calculate_multiple_of_three_percentage(num_rolls)

    # Printed Output
    print("---------------- Dice Roll Simulation ----------------")
    print(f"Rolled the dice {num_rolls} times.")
    print(f"Percentage of rolls with a sum that is a multiple of 3: {percentage:.2f}%")
    print("------------------------------------------------------")

# Run the program
if __name__ == "__main__":
    main()
