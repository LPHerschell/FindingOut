# specify the file name and location where you want to save the text file
file_path = "/PythonPractice/w/ReadMe.txt"

# create a text file with "your mom" written inside
with open(file_path, 'w') as file:
    file.write("your mom")
