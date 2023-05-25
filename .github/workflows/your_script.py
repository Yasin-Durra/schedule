import datetime

# Get the current date
current_date = datetime.date.today()

# Convert the date to a string representation
date_str = current_date.strftime("%Y-%m-%d")

# Open the file in append mode (creates the file if it doesn't exist)
file_path = "date_file.txt"  # Specify the file path or name here
with open(file_path, "a") as file:
    # Write the date to the file
    file.write(date_str + "\n")

print("Date written to file:", date_str)