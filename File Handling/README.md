# File Handling in Python

File handling in Python is a crucial aspect of programming, allowing you to work with files on your computer. Whether it's reading data from a file, writing data to a file, or manipulating files in various ways, Python provides powerful tools and functionalities to handle these operations efficiently.

This README will cover the basics of file handling in Python, including reading from and writing to files, working with different file modes, and handling exceptions.

## 1. Opening and Closing Files

In Python, you use the `open()` function to open a file. It requires at least one argument - the name of the file you want to open. Optionally, you can specify the mode in which you want to open the file.

```python
# Opening a file in read mode
file = open("example.txt", "r")

# Closing the file
file.close()
```

It's important to close the file after you're done working with it to release the system resources associated with it.

## 2. Reading from Files

Python provides several methods to read data from a file:

- `read()`: Reads the entire content of the file.
- `readline()`: Reads a single line from the file.
- `readlines()`: Reads all lines from the file and returns them as a list.

```python
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
```

## 3. Writing to Files

To write data to a file, you need to open it in write mode (`"w"`). If the file doesn't exist, Python will create it. If it already exists, Python will overwrite its contents.

```python
file = open("example.txt", "w")
file.write("Hello, World!\n")
file.close()
```

## 4. Appending to Files

To append data to an existing file, you can open it in append mode (`"a"`).

```python
file = open("example.txt", "a")
file.write("Appending new data!\n")
file.close()
```

## 5. File Modes

Here are some common file modes in Python:

- `"r"`: Read mode (default).
- `"w"`: Write mode - overwrites the file if it exists, creates a new file if it doesn't.
- `"a"`: Append mode - appends to the end of the file.
- `"b"`: Binary mode - for working with binary files (e.g., images, videos).
- `"t"`: Text mode (default) - for working with text files.

You can combine modes by adding them together (e.g., `"rb"`, `"w+"`, etc.).

## 6. Exception Handling

When working with files, it's important to handle exceptions, especially when opening, reading, or writing files. Common exceptions include `FileNotFoundError`, `PermissionError`, etc.

```python
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()
```

Using a `try`-`except` block ensures that your code doesn't crash if an exception occurs while working with files.

## 7. Create a New File

To create a new file in Python, use the `open()` method, with one of the following parameters:

- `"x"` - Create: will create a file, returns an error if the file exists.
- `"a"` - Append: will create a file if the specified file does not exist.
- `"w"` - Write: will create a file if the specified file does not exist.

### Example

Create a file called "myfile.txt":

```python
f = open("myfile.txt", "x")

Create a new file if it does not exist:
f = open("myfile.txt", "w")

## 8. Python Delete File

### Delete a File

To delete a file, you must import the OS module and run its os.remove() function:

#### Example

Remove the file "demofile.txt":

import os
os.remove("demofile.txt")

## Check if File Exists

To avoid getting an error, you might want to check if the file exists before you try to delete it:

#### Example

Check if the file exists, then delete it:

# python
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")

## Delete Folder

To delete an entire folder, use the os.rmdir() method:

#### Example

Remove the folder "myfolder":

python
import os
os.rmdir("myfolder")


## Conclusion

File handling is an essential part of Python programming. Understanding how to open, read from, write to, and close files, along with proper exception handling, will enable you to work effectively with files in your Python projects. Experiment with different file operations and modes to become proficient in file handling.
