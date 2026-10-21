import csv

missing_count = 0
clean_students = []

with open("02_Projects/01_Student_Data_Cleaning/students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for student in reader:
        if student["Maths"] == "" or student["Science"] == "" or student["English"] == "":
            missing_count += 1
            print("Skipping incomplete record:", student["Name"])
        else:
            clean_students.append(student)

print("Total records with missing values:", missing_count)
print("Records remaining:", len(clean_students))

student_ids = set()
duplicate_count = 0
unique_students = []

for student in clean_students:
    student_id = student["Student_ID"]

    if student_id in student_ids:
        duplicate_count += 1
        print("Skipping duplicate:", student["Name"], student_id)
    else:
        student_ids.add(student_id)
        unique_students.append(student)

print("Total duplicate records:", duplicate_count)
print("Unique student records:", len(unique_students))

invalid_count = 0
valid_students = []

for student in unique_students:
    maths = int(student["Maths"])
    science = int(student["Science"])
    english = int(student["English"])

    if (
        maths < 0 or maths > 100
        or science < 0 or science > 100
        or english < 0 or english > 100
    ):
        invalid_count += 1
        print("Skipping invalid record:", student["Name"])
    else:
        valid_students.append(student)

print("Total records with invalid marks:", invalid_count)
print("Total valid student records:", len(valid_students))

print("\nStudent Performance Analysis")
print("----------------------------")

for student in valid_students:
    maths = int(student["Maths"])
    science = int(student["Science"])
    english = int(student["English"])

    total = maths + science + english
    average = total / 3

    student["Total"] = total
    student["Average"] = round(average, 2)

    print(
        student["Name"],
        "| Total:", student["Total"],
        "| Average:", student["Average"]
    )
output_file = "02_Projects/01_Student_Data_Cleaning/cleaned_students.csv"

fieldnames = [
    "Student_ID",
    "Name",
    "Maths",
    "Science",
    "English",
    "Total",
    "Average"
]

with open(output_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(valid_students)

print("\nCleaned CSV file created successfully!")
print("Total records exported:", len(valid_students))
