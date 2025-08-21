#Takes user input and writes it to a file named output.txt
input_1 = input("Enter text to write to the file: ")
try:
    file_1 = open("Output.txt", "w")
    file_1.write(input_1)
    print("Data successfully written to Output.txt")
    file_1.close()
except FileNotFoundError:
    print("File Output.txt not found")

# Appends additional data to the same file
input_2 = input("Enter additional text to append: ")
try:
    file_2 = open("Output.txt", "a")
    file_2.write("\n")
    file_2.write(input_2)
    print("Data successfully appended.")
    file_2.close()
except FileNotFoundError:
    print("File Output.txt not found")

# Reads and displays the final content of the file
try:
    read_file = open("Output.txt", "r")
    file_data = read_file.read()
    print("Final content of output.txt:")
    print(file_data)
    read_file.close()
except FileNotFoundError:
    print("File Output.txt not found")