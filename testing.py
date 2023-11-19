
import os

# Navigate to the parent directory
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define the path to the file you want to access
file_path = os.path.join(parent_directory, "wordfiles", "englishwords.txt")

# Check if the file exists
if os.path.exists(file_path):
    # If the file exists, you can open and read it
    with open(file_path, "r") as file:
        file_content = file.read()
        print("File Content:")
        print(file_content)
else:
    print("The specified file does not exist.")