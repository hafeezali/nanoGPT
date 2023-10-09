# List of allowed characters
allowed_chars = "!$&',-.3:;?ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz \n"

# Input file and output file paths
input_file_path = "tt_7_5k.txt"
output_file_path = "tt_7_5k_filtered.txt"

# Read the content of the input file
with open(input_file_path, "r") as input_file:
    content = input_file.read()

# Initialize an empty string to store the result
result_string = ""

# Iterate through each character in the content
for char in content:
    # Check if the character is in the list of allowed characters
    if char in allowed_chars:
        # If it's allowed, add it to the result string
        result_string += char

# Write the result string back to the output file
with open(output_file_path, "w") as output_file:
    output_file.write(result_string)

