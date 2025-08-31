# File Read & Write Challenge

# Open the original file in read mode
with open("context.txt", "r") as file:
    content = file.read()
    print(content)

# Modify the content (example: make all text uppercase)
modified_content = content.upper()

# Write the modified content into a new file
with open("modified_context.txt", "w") as new_file:
    new_file.write(modified_content)

print("File has been read, modified, and written to 'modified_context.txt'")