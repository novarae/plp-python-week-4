# Error Handling Lab

try:
    # Ask the user for the filename
    filename = input("Enter the filename: ")

    # Try opening the file
    with open(filename, "r") as file:
        content = file.read()
        print("\n File content:\n")
        print(content)

except FileNotFoundError:
    print("Error: File not found. Please check the filename and try again.")
except PermissionError:
    print("Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
