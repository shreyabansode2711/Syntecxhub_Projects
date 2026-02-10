
import csv
import os

FILE_NAME = "students.csv"


class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade


class StudentManager:
    def __init__(self):
        self.students = {}
        self.load_students()

    def load_students(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        sid, name, grade = row
                        self.students[sid] = Student(sid, name, grade)

    def save_students(self):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            for student in self.students.values():
                writer.writerow(
                    [student.student_id, student.name, student.grade])

    def add_student(self):
        sid = input("Enter Student ID: ")
        if sid in self.students:
            print("Student ID already exists.")
            return
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        self.students[sid] = Student(sid, name, grade)
        self.save_students()
        print("Student added successfully.")

    def update_student(self):
        sid = input("Enter Student ID to update: ")
        if sid not in self.students:
            print("Student not found.")
            return
        self.students[sid].name = input("Enter new Name: ")
        self.students[sid].grade = input("Enter new Grade: ")
        self.save_students()
        print("Student updated successfully.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")
        if sid in self.students:
            del self.students[sid]
            self.save_students()
            print("Student deleted.")
        else:
            print("Student not found.")

    def list_students(self):
        if not self.students:
            print("No student records available.")
            return
        for student in self.students.values():
            print(
                f"ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")


def main():
    manager = StudentManager()
    while True:
        print("\n1.Add 2.Update 3.Delete 4.List 5.Exit")
        choice = input("Select option: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.update_student()
        elif choice == "3":
            manager.delete_student()
        elif choice == "4":
            manager.list_students()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")


main()