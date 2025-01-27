import re
import json

class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def calculate_grade(self, subject, grading_scale):
        if subject not in self.scores:
            return "N/A"  # Not Applicable
        score = self.scores[subject]
        for grade, threshold in grading_scale.items():
            if score >= threshold:
                return grade
        return "Fail"

    def to_dict(self):
        return {"name": self.name, "scores": self.scores}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["scores"])


def validate_score(score):
    return re.match(r"^\d+$", str(score)) and 0 <= int(score) <= 100 #only accepts numbers between 0 and 100


def save_grades(students, filename="grades.json"):
    data = [student.to_dict() for student in students]
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def load_grades(filename="grades.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return [Student.from_dict(student_data) for student_data in data]
    except FileNotFoundError:
        return []

def main():
    grading_scale = {"A": 90, "B": 80, "C": 70, "D": 60, "E": 50}
    students = load_grades()

    while True:
        print("\nGrade Calculator")
        print("1. Add Student")
        print("2. View Grades")
        print("3. Save Grades")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter student name: ")
            scores = {}
            while True:
                subject = input("Enter subject (or type 'done'): ")
                if subject.lower() == "done":
                    break
                while True:
                    score_str = input(f"Enter {subject} score: ")
                    if validate_score(score_str):
                        scores[subject] = int(score_str)
                        break
                    else:
                        print("Invalid score. Please enter a number between 0 and 100.")

            students.append(Student(name, scores))

        elif choice == "2":
            if not students:
                print("No students added yet.")
            else:
                print("\nStudent Grades:")
                for student in students:
                    print(f"\nName: {student.name}")
                    for subject in student.scores:
                        grade = student.calculate_grade(subject, grading_scale)
                        print(f"{subject}: Score: {student.scores[subject]}, Grade: {grade}")

        elif choice == "3":
            save_grades(students)
            print("Grades saved to grades.json")

        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()






