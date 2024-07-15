import pandas as pd
import re
from datetime import datetime

# Function to convert dates to yyyy-mm-dd format, or yyyy-mm, or yyyy
def convert_to_yyyy_mm_dd(date_str):
    if date_str is None:
        return None
    # Define possible date formats and their corresponding output formats
    date_formats = [
        ("%b-%y", "%Y-%m"),        # Mar-91 to yyyy-mm
        ("%Y", "%Y"),              # 1991 to yyyy
        ("%m/%d/%y", "%Y-%m-%d"),  # 4/27/97 to yyyy-mm-dd
        ("%m/%d/%Y", "%Y-%m-%d")   # 5/5/1996 to yyyy-mm-dd
    ]
    
    for fmt, out_fmt in date_formats:
        try:
            return datetime.strptime(date_str, fmt).strftime(out_fmt)
        except ValueError:
            continue
    return None

# Step 1: Read the CSV file
file_path = 'date formatting/your_file.csv'
df = pd.read_csv(file_path)

# Step 2: Extract dates using regex
def extract_date(recording_str):
    if not isinstance(recording_str, str):
        return None
    # Patterns to match different date formats amidst other text
    patterns = [
        r'\d{1,2}/\d{1,2}/\d{4}',   # 5/5/1996 or 7/21/1987
        r'\d{1,2}/\d{1,2}/\d{2}',   # 4/27/97
        r'\w{3}-\d{2}',             # Mar-91
        r'\d{4}'                    # 1991
    ]
    
    for pattern in patterns:
        match = re.search(pattern, recording_str)
        if match:
            return match.group()
    return None

# Extract date strings
df['Date Extracted'] = df['Recording Date and Location'].apply(extract_date)

# Step 3: Convert extracted dates to yyyy-mm-dd, yyyy-mm, or yyyy format
df['Formatted Date'] = df['Date Extracted'].apply(convert_to_yyyy_mm_dd)

# Drop the intermediate column if not needed
df.drop(columns=['Date Extracted'], inplace=True)

# Step 4: Save the modified DataFrame to a new CSV file
output_file_path = 'date formatting/output.csv'
df.to_csv(output_file_path, index=False)

# Display the modified DataFrame
print(df[['Recording Date and Location', 'Formatted Date']])
