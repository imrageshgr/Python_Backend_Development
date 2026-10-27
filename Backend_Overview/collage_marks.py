
# Student records
students = {
    "101": {"name": "Arun", "marks": 85},
    "102": {"name": "Priya", "marks": 92},
    "103": {"name": "Ravi", "marks": 74}
}

# Receive the request
register_number = input("Enter register number: ")

# Process the request
if register_number in students:
    student = students[register_number]

    # Send the response
    print("Student:", student["name"])
    print("Python marks:", student["marks"])
else:
    print("Error: Student not found")
