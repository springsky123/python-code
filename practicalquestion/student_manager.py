
import csv
import os

# Custom exception for invalid score input
class InvalidScoreError(Exception):
    pass

def add_student_data():
    """
    Adds a new student's name and score to the CSV file.
    Ensures score is between 0 and 100, and handles invalid input.
    Adds headers if the file is empty.
    """
    while True:
        try:
            name = input("Enter student name: ").strip()
            score = int(input("Enter student score (0-100): ").strip())
            if not (0 <= score <= 100):
                raise InvalidScoreError("Invalid score")
            break  # Input is valid, break loop
        except ValueError:
            print("Invalid value for score! Please enter a number between 0 and 100.")
        except InvalidScoreError as e:
            print(e, "Please try again.")

    # Check if file exists and if header needs to be written
    file_exists = os.path.isfile("student.csv")
    write_header = not file_exists or os.path.getsize("student.csv") == 0

    # Write student data to CSV
    with open("student.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(["Name", "Score"])
        writer.writerow([name, score])
        print("Student data added successfully.")

def class_average():
    """
    Calculates and prints the average score of all students from the CSV file.
    Handles the case when no data is present.
    """
    try:
        with open("student.csv", "r", newline="") as file:
            reader = csv.DictReader(file)
            scores = [int(row["Score"]) for row in reader if row.get("Score")]
            if scores:
                average = sum(scores) / len(scores)
                print("Average score:", average)
            else:
                print("No student data found.")
    except FileNotFoundError:
        print("File not found. Please add some student data first.")

def get_top_students(filename="student.csv", num_top=3):
    """
    Returns a list of the top N students by score from the CSV file.
    Skips rows with missing or invalid scores.
    """
    students = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    row["Score"] = int(row["Score"])
                    students.append(row)
                except (ValueError, KeyError):
                    print(f"Skipping row due to invalid or missing score: {row}")
        # Sort students by score in descending order
        students.sort(key=lambda x: x["Score"], reverse=True)
        return students[:num_top]
    except FileNotFoundError:
        print("File not found. Please add some student data first.")
        return []

def choose_option():
    """
    Presents the user with menu options and returns their choice.
    Ensures user input is valid.
    """
    print('......................................')
    print("1. Add student data")
    print("2. Calculate average")
    print("3. Print Top 3 students")
    print('.......................................')
    while True:
        try:
            choice = int(input('Enter your choice: ').strip())
            return choice
        except ValueError:
            print("Invalid input! Please enter a number (1-3).")

def main():
    """
    Main program loop to handle user interaction.
    Allows the user to add data, calculate average, or print top students.
    """
    print("------------------WELCOME TO THIS PROGRAM-----------------")
    while True:
        opt = choose_option()
        if opt == 1:
            add_student_data()
        elif opt == 2:
            class_average()
        elif opt == 3:
            top_students = get_top_students()
            print("Top 3 Students:")
            for student in top_students:
                print(f"Name: {student['Name']}, Score: {student['Score']}")
        else:
            print("Invalid choice! Please try again.")
        print()
        cont = input('Do you want to continue? (type y for yes): ').strip().lower()
        if cont != 'y':
            break
    print("\nThank you for visiting this program...")

if __name__ == "__main__":
    main()
