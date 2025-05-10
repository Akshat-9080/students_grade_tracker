# Student Grade Tracker

# Dictionary to store grades
grades = {}

# Function to input grades
def input_grades():
    while True:
        subject = input("Enter subject name (or type 'done' to finish): ")
        if subject.lower() == 'done':
            break
        grade = float(input(f"Enter grade for {subject}: "))
        grades[subject] = grade

# Function to calculate average
def calculate_average():
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

# Function to display results
def display_results():
    print("\nStudent Grades:")
    for subject, grade in grades.items():
        print(f"{subject}: {grade}")
    print(f"\nAverage Grade: {calculate_average():.2f}")

# Running the program
input_grades()
display_results()