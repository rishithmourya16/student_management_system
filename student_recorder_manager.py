import re


class InvalidEmailException(Exception):
    pass


class Student:
    def __init__(self, student_id, name, email, course, marks):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.course = course
        self.marks = marks

    def __str__(self):
        return f"{self.student_id},{self.name},{self.email},{self.course},{self.marks}"


class StudentManager:
    def __init__(self):
        self.students = []

    def validate_email(self, email):
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if not re.match(pattern, email):
            raise InvalidEmailException("Invalid Email Format!")

    def add_student(self):
        try:
            student_id = int(input("Enter Student ID: "))

            # Check duplicate ID
            for student in self.students:
                if student.student_id == student_id:
                    print("Student ID already exists!")
                    return

            name = input("Enter Name: ").strip()
            email = input("Enter Email: ").strip()
            course = input("Enter Course: ").strip()
            marks = float(input("Enter Marks: "))

            if not name or not course:
                raise ValueError("Name and Course cannot be empty.")

            self.validate_email(email)

            student = Student(student_id, name, email, course, marks)
            self.students.append(student)

            print("Student added successfully!")

        except ValueError as e:
            print("Invalid Input:", e)

        except InvalidEmailException as e:
            print(e)

    def view_students(self):
        if not self.students:
            print("No student records found.")
            return

        print("\n----- Student Records -----")
        for student in self.students:
            print(student)

    def save_to_file(self):
        try:
            with open("students.txt", "w") as file:
                for student in self.students:
                    file.write(str(student) + "\n")

            print("Student data saved successfully!")

        except Exception as e:
            print("Error while saving file:", e)

    def read_from_file(self):
        try:
            with open("students.txt", "r") as file:
                data = file.readlines()

            if not data:
                print("File is empty.")
                return

            print("\n----- Student Data from File -----")
            for line in data:
                print(line.strip())

        except FileNotFoundError:
            print("students.txt not found.")

        except Exception as e:
            print("Error:", e)


def main():
    manager = StudentManager()

    while True:
        print("\n===== Student Record Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Data to File")
        print("4. Read Student Data")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                manager.add_student()

            elif choice == 2:
                manager.view_students()

            elif choice == 3:
                manager.save_to_file()

            elif choice == 4:
                manager.read_from_file()

            elif choice == 5:
                print("Thank you!")
                break

            else:
                print("Please enter a valid choice.")

        except ValueError:
            print("Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()