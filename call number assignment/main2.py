import pandas as pd

# Load the Excel file
df = pd.read_csv('call number assignment/data.csv')  

# Initialize variables
current_call_number = 12769
previous_part = 0

# List to store the generated call numbers
call_numbers = []

for index, row in df.iterrows():
    part = row['Part']
    if pd.isna(part):
        # If there's no part number, just assign the current call number
        current_call_number += 1
        call_numbers.append(str(current_call_number))
        # current_call_number += 1  # Increment for the next row
    else:
        part = int(part)
        if part == 1:
            # Start of a new multi-part CD, assign and increment for the next first part
            current_call_number += 1
            call_numbers.append(f"{current_call_number}({part})")
            previous_part = part
        else:
            # Continuing a multi-part CD, do not increment
            if previous_part == 1:
                previous_call_number = current_call_number
            call_numbers.append(f"{previous_call_number}({part})")
            previous_part = part

# Add the call numbers to the DataFrame
df['Call Number'] = call_numbers

df.to_csv('call number assignment/modified_data.csv', index=False)
