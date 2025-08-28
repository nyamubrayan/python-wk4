# File Read & Write with Error Handling

## Description
This Python program reads the content of a user-specified file, modifies it, and writes the modified content to a new file. It also handles errors gracefully, such as when the file does not exist or cannot be accessed.  

The example modification implemented converts all text to uppercase, but it can be easily customized.

---

## Features
- Reads a file provided by the user.
- Modifies each line of the file (currently converts text to uppercase).
- Writes the modified content to a new file prefixed with `modified_`.
- Handles common errors:
  - File not found
  - Permission errors
  - Other unexpected exceptions

---

## Requirements
- Python 3.x
- No additional libraries required

---

## Usage
1. Run the Python script:
    ```bash
    python file_read_write.py
    ```
2. Enter the name of the file you want to read.
3. The modified file will be created in the same directory with the prefix `modified_`.

---

## Example
If the input file `example.txt` contains:
