try:
    file_1 = open('sample.txt', 'r')
    line_number = 1
    print("Reading file content:")
    for line in file_1:
        print(f"Line {line_number}:", line.strip())
        line_number += 1
except FileNotFoundError:
    print("The file 'sample.txt' was not found")