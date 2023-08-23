# Define a variable
interest_level = 5

# Function to check interest level
def check_interest(level):
    if level > 5:
        return "Very Interesting!"
    else:
        return "Moderately Interesting."

# Function to double the interest level
def double_interest(level):
    return level * 2

# Loop to modify interest levels
for i in range(3):
    interest_level = double_interest(interest_level)
    print(f"Interest level after iteration {i+1}: {interest_level}")

# Write interest level to a file
with open("interest.txt", "w") as file:
    file.write(str(interest_level))

# Read and display the content of the file
with open("interest.txt", "r") as file:
    file_content = file.read()
    print("Interest level from file:", file_content)