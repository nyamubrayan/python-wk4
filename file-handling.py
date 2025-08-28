# File Read & Write with Error Handling in Python

def modify_content(line):
    """
    Modify the content of a line before writing to a new file.
    Example: convert text to uppercase.
    """
    return line.upper()

def main():
    try:
        # Ask user for the input filename
        input_file = input("Enter the name of the file to read: ")

        # Open the input file for reading
        with open(input_file, 'r') as file:
            content = file.readlines()  # Read all lines

        # Modify content
        modified_content = [modify_content(line) for line in content]

        # Define output filename
        output_file = "modified_" + input_file

        # Write modified content to new file
        with open(output_file, 'w') as file:
            file.writelines(modified_content)

        print(f"Modified content has been written to '{output_file}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist. Please check the filename.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write the file '{input_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
