# by GPT 4o-mini 1.19.2025

import re
import csv

# Define the path to the text file
file_path = "directory.txt"
output_csv = "students.csv"

# Define a function to extract student information using regex
def extract_students_from_text(file_path):
    students = []
    
    # Read the text file
    with open(file_path, "r") as file:
        text = file.read()
        
        # Regex to match student entries
        matches = re.findall(
            r"(\w+),\s(\w+)\s+Grad Year:\s(\d{4})", text
        )
        
        # Extract and store student information
        for match in matches:
            last_name, first_name, grad_year = match
            students.append({
                "Student": f"{first_name} {last_name}",
                "Grad Year": grad_year
            })
    # Sort students by graduation year
    students.sort(key=lambda x: x["Grad Year"])
    return students

# Extract students from the text file
students = extract_students_from_text(file_path)

# Write the sorted student data to a CSV file
with open(output_csv, mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["Student", "Grad Year"], extrasaction='ignore')
    writer.writeheader()
    writer.writerows(students)

print(f"Student data has been exported to {output_csv}")