# File creation, writing to a file
try:
    # Create a new file "my_file.txt" in write mode
    with open("my_file.txt", 'w') as file:
        # Writing three lines of text
        file.write("Hello, this is the first line.\n")
        file.write("The number is 18.\n")
        file.write("This is another example of text with a number: 200.\n")

    # Reading and displaying the contents
    with open("my_file.txt", 'r') as file:
        print("Contents of 'my_file.txt' after writing:")
        print(file.read())

    # Appending additional lines to the file
    with open("my_file.txt", 'a') as file:
        file.write("Here is an appended line.\n")
        file.write("Appending another number: 100.\n")
        file.write("Final appended line with text and a number: 700.\n")

    # Reading and displaying the contents of the file after appending
    with open("my_file.txt", 'r') as file:
        print("\nContents of 'my_file.txt' after appending:")
        print(file.read())

# Error handling for potential file-related exceptions
except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to access the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile handling operations complete.")
