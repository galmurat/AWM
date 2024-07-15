# This code parses through a spreadsheet (which you can export from Excel as a csv file) and cleans it up. 
# It moves the contact informaiton into different columns, cleaning it. 
# Input the file you want to clean as "yourfile.csv" and the cleaned up version will be named "updated_file.csv"

import pandas as pd
import re

def extract_info(history_note):
    address = re.search(r"Address: (.*?)(?=, Phone:|, E-mail:|, Fax:|Phone/Fax:|Phone & Fax:|$)", history_note)
    phone = re.search(r"Phone: (.*?)(?=, Fax:|, E-mail:|, Address:|$)", history_note)
    fax = re.search(r"Fax: (.*?)(?=, E-mail:|, Address:|$)", history_note)
    email = re.search(r"E-mail: (.*?)(?=, Phone:|, Fax:|, Address:|$)", history_note)

    # Handling cases where phone and fax are the same
    phone_fax = re.search(r"Phone/Fax: (.*?)(?=, E-mail:|$)", history_note)
    phone_and_fax = re.search(r"Phone & Fax: (.*?)(?=, E-mail:|$)", history_note)

    if phone_fax:
        phone_number = phone_fax.group(1).strip()
        fax_number = phone_number
    elif phone_and_fax:
        phone_number = phone_and_fax.group(1).strip()
        fax_number = phone_number
    else:
        phone_number = phone.group(1).strip() if phone else ''
        fax_number = fax.group(1).strip() if fax else ''

    return {
        'Address': address.group(1).strip() if address else '',
        'Phone': phone_number,
        'Fax': fax_number,
        'Email': email.group(1).strip() if email else ''
    }

def clean_up_column(column, patterns):
    if isinstance(column, str):
        for pattern in patterns:
            column = re.sub(pattern, '', column).strip()
    return column

df = pd.read_csv('music labels data cleaning/yourfile.csv')

df.columns = df.columns.str.strip()
print("Columns:", df.columns)

df['Address'] = ''
df['Phone'] = ''
df['Fax'] = ''
df['Email'] = ''

for idx, row in df.iterrows():
    if pd.notna(row['History Note']):
        info = extract_info(row['History Note'])
        df.at[idx, 'Address'] = info['Address']
        df.at[idx, 'Phone'] = info['Phone']
        df.at[idx, 'Fax'] = info['Fax']
        df.at[idx, 'Email'] = info['Email']

patterns_history_note = [r'Address:.*', r'Phone:.*', r'Fax:.*', r'E-mail:.*']
patterns_address = [r'Phone:.*', r'Fax:.*', r'E-mail:.*', r'Phone/Fax:.*', r'Phone & Fax:.*']
patterns_phone = [r'Fax:.*', r'E-mail:.*']
patterns_fax = [r'E-mail:.*']

df['History Note'] = df['History Note'].apply(lambda x: clean_up_column(x, patterns_history_note))
df['Address'] = df['Address'].apply(lambda x: clean_up_column(x, patterns_address))
df['Phone'] = df['Phone'].apply(lambda x: clean_up_column(x, patterns_phone))
df['Fax'] = df['Fax'].apply(lambda x: clean_up_column(x, patterns_fax))
df['Email'] = df['Email'].apply(lambda x: clean_up_column(x, [r'E-mail:.*']))

df.to_csv('music labels data cleaning/updated_file.csv', index=False)

print("Data has been successfully processed and saved to 'updated_file.csv'.")
