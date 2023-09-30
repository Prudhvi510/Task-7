import datetime

def create_timestamp_file():
    # Get the current timestamp
    current_time = datetime.datetime.now()
    
    # Format the timestamp as a string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create a filename with the timestamp
    filename = f"{timestamp_str}.txt"
    
    # Create the file
    with open(filename, 'w') as file:
        pass  # You can add content to the file if needed

if __name__ == "__main__":
    create_timestamp_file()
    print("Timestamp file created successfully.")