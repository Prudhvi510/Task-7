import datetime

def create_timestamp_file_with_content():
    # Get the current timestamp
    current_time = datetime.datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a filename with the timestamp
    filename = f"{timestamp_str}.txt"
    
    # Create the file and write the timestamp as its content
    with open(filename, 'w') as file:
        file.write(timestamp_str)

if __name__ == "__main__":
    create_timestamp_file_with_content()
    print("Timestamp file created successfully.")