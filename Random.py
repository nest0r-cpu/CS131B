# Function to simulate rolling a dices
def roll_die(sides):
    # Simulate random side function
     return (hash(str(sides)) % sides) + 1

# Roll the 9-sided die (1-9)
nine_sided_die = roll_die(9)

# Roll the 9000-sided die (1-9000)
nine_thousand_sided_die = roll_die(9000)

# Sum of the results
total = nine_sided_die + nine_thousand_sided_die

# Is a multiple of three?
is_multiple_of_three = total % 3 == 0

# Output the results with context
print("---------------- Dice Roll Simulation ----------------")
print()
print("RULES")
print("Number 1. is a 9-sided die (with sides numbered 1 to 9)")
print("Number 2. is a 9000-sided die (with sides numbered 1 to 9000)")
print()
print(" *******You Have rolled two dice:*******")
print(f"1. 9-sided die... You rolled: {nine_sided_die}")
print(f"2. 9000-sided die... You rolled: {nine_thousand_sided_die}")
print()
print(f"The sum of your rolls is: {total}")

# Output if the sum result is multiple of three
if is_multiple_of_three:
    print("Congratulations! The sum is a multiple of three.")
else:
    print("The sum is not a multiple of three. Better luck next time!")

print("----------------------------------------------------------")
