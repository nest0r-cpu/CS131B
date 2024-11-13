import sys

# Checking if there are command line arguments passed
if len(sys.argv) < 2:
    print("Error: No command line arguments provided.")
    sys.exit(1)  # Exiting the program with a error code

# Checking if the first command line argument can be converted into a float
try:
    float(sys.argv[1])  # Converting the first argument to a float
except ValueError:
    print("Error: The first argument should be a valid number. For example, '1' or '23.4'. Please avoid using any letters or symbols.")
    sys.exit(1)  # Exiting the program with an error code

# To initialize a variable to store the sum
total = 0

# Loop the command line arguments, starting from the second argument
for arg in sys.argv[1:]:
    try:
        # Converting the argument to an integer and then adding it to the total
        total += int(arg)
    except ValueError:
        # Ignore if the argument cannot be converted to an integer.
        pass

# Print the sum of valid integers
print("Sum of integer arguments:", total)
