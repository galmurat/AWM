# AWM
This repository contains code from summer 2024 simplifying certain processes. Each document entails a detailed description of what the code does, how to run it, along with a video showing how to do it. Here's a quick description of what each document does:

# Call number assignment 
When input a csv file which has a "Parts" column, outputs assigned call numbers which include the part in parenthesis. For example, it will output AWM SC 10000(1). 

The only things you must do is put in a csv file into the call number assignment folder titled data.csv and change the "current call number" at the very top of the code. The output is the modified_case.csv file. 

# Date formatting 
When input a csv file which has a "Date" column, outputs only the date (removing irrelevant information) in the format yyyy-mm-dd. 

The only things you must do is put in a csv file into the date formatting folder titled your_file.csv The output is output.csv 

# Music labels data cleaning
When you input a CSV file which contains a "History Note" column, this code extracts and organizes contact information such as addresses, phone numbers, fax numbers, and email addresses into separate columns. For example, it will move "Phone: 123-456-7890" from the "History Note" column to the new "Phone" column.

The only things you must do are input a CSV file into the "music labels data cleaning" folder titled "yourfile.csv" and run the code. The output is the "updated_file.csv" file.

# Template Labeling
There's two parts to this code. You will choose which code to run depending on your case. 
1. Non-sequential ordering of the call numbers /n
If the call numbers are not in direct ascending order but have multiple parts (e.g. AWM SC 12(1), AWM SC 12(2), AWM Sc 13) or you want control over which specific numbers will be put in (e.g. AWM SC 4, AWM SC 6, AWM SC 9, AWM SC 13), you will use the non-sequential.py file. To use it, copy over the specific call numbers you want inside the brackets in the "values" variable at the top, seperating them with commas and quotation marks. The output will be in the output folder in the template labeling folder. 

2. Sequential ordering of the call numbers /n
If the call numbers are in direct ascending order (e.g. AWM SC 1, AWM SC 2, AWM SC 3, AWM SC 4), then you wil use the sequential.py file. Simply input the first and last number you want labeled. The output will be in the template labeling folder. 
