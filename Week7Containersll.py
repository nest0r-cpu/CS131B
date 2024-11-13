import sys

# Get command line arguments & starting from index 1
args = sys.argv[1:]

# Removes duplicates
unique_args = set(args)

# Sort the arguments alphabetically
sorted_args = sorted(unique_args)

# Print each argument on a new line
for arg in sorted_args:
    print(arg)
