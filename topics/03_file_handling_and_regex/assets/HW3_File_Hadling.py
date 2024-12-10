original_file_path = r'file1_cars.txt'
new_file_path = r'file2_cars.txt'
combined_file_path = r'combined_cars.txt'

# Read the file
with open(original_file_path, 'r') as file:
    content = file.readlines()

# Print the contents to see what was read
print(content)

# Remove equal lines
unique_lines = set(content)

# Save the result in the new file
with open(new_file_path, 'w') as file:
    for line in unique_lines:
        file.write(line)

# Open the first file and read its contents
with open(original_file_path, 'r') as file1:
    content1 = file1.readlines()

# Open the second file and read its contents
with open(new_file_path, 'r') as file2:
    content2 = file2.readlines()

# Combine the contents of the two files
combined_content = content1 + content2

# Write the combined content to the third file
with open(combined_file_path, 'w') as combined_file:
    combined_file.writelines(combined_content)
