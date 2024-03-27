try:
    # Creates a new file and writes data to it
    with open("myfile.txt", "w") as f:
        f.write("The open() function opens the file named 'example.txt' in read mode ('r').\n")
        f.write("We can perform operations like reading the file's contents or iterating over its lines.\n")
        f.write("Appending new data!\n")

    # Open the file for reading
    with open("myfile.txt", "r") as f:
        # Read and display the contents of the file
        content = f.read()
        print(content)

    # File appending
    with open("myfile.txt", 'a') as f:
        f.write('After writing data to the file, the script reopens "myfile.txt" in read mode to access its contents \n')
        f.write("Using the read() method, the script reads the entire content of the file into the variable \n")
        f.write("the script appends data \n")

except FileNotFoundError:
    print("File not found. Please check the file path.")

except PermissionError:
    print("Permission denied. Please check file permissions.")

except Exception as e:
    print("An error occurred:", e)

finally:
    # Clean-up code: Close the file if it was opened
    if 'f' in locals():
        f.close()
