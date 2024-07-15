import pandas as pd
import re
from datetime import datetime

# Function to convert dates to yyyy-mm-dd format, or yyyy-mm, or yyyy
def convert_to_yyyy_mm_dd(date_str):
    if date_str is None:
        return None
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

df['Date Extracted'] = df['Recording Date and Location'].apply(extract_date)

df['Formatted Date'] = df['Date Extracted'].apply(convert_to_yyyy_mm_dd)

df.drop(columns=['Date Extracted'], inplace=True)

output_file_path = 'date formatting/output.csv'
df.to_csv(output_file_path, index=False)

print(df[['Recording Date and Location', 'Formatted Date']])
