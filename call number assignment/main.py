import pandas as pd

df = pd.read_csv('call number assignment/data.csv')

# Input the first call number you want to start with. 
current_call_number = 12769
previous_part = 0

call_numbers = []

for index, row in df.iterrows():
    part = row['Part']
    if pd.isna(part):
        current_call_number += 1
        call_numbers.append(f"AWM SC {current_call_number}")
    else:
        part = int(part)
        if part == 1:
            current_call_number += 1
            call_numbers.append(f"AWM SC {current_call_number}({part})")
            previous_part = part
        else:
            if previous_part == 1:
                previous_call_number = current_call_number
            call_numbers.append(f"AWM SC {previous_call_number}({part})")
            previous_part = part

df['Call Number'] = call_numbers

df.to_csv('call number assignment/modified_data.csv', index=False)

