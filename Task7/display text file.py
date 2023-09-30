def read_and_display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            file_content = file.read()
            print("File Content:")
            print(file_content)
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    read_and_display_file_content(file_name)