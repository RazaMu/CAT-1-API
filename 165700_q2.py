# Online Course Management System
# This program implements a basic system for managing students and assignments in an online course

class Student:
    """
    Student class to represent a student in the course
    Attributes:
        name: Name of the student
        student_id: Unique ID for the student
        assignments: Dictionary storing assignment names and grades
    """
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Empty dictionary to store assignments and grades
    
    def add_assignment_grade(self, assignment_name, grade):
        """Add or update a grade for an assignment"""
        self.assignments[assignment_name] = grade
    
    def display_grades(self):
        """Display all assignments and grades for the student"""
        print(f"\nGrades for {self.name} (ID: {self.student_id}):")
        if not self.assignments:
            print("No assignments graded yet.")
        else:
            # Calculate average grade
            total_grade = sum(self.assignments.values())
            average = total_grade / len(self.assignments)
            
            # Display individual grades
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
            print(f"Average grade: {average:.2f}")
    
    def __str__(self):
        """String representation of the student"""
        return f"{self.name} (ID: {self.student_id})"

class Instructor:
    """
    Instructor class to manage the course and students
    Attributes:
        name: Name of the instructor
        course_name: Name of the course
        students: List of students in the course
    """
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # Empty list to store students
    
    def add_student(self, name, student_id):
        """
        Add a new student to the course
        Returns the created student object
        """
        # Check if student ID already exists
        if any(student.student_id == student_id for student in self.students):
            print("Error: Student ID already exists!")
            return None
        
        student = Student(name, student_id)
        self.students.append(student)
        return student
    
    def assign_grade(self, student_id, assignment_name, grade):
        """Assign a grade to a student's assignment"""
        student = self.find_student(student_id)
        if student:
            student.add_assignment_grade(assignment_name, grade)
            return True
        return False
    
    def find_student(self, student_id):
        """Find a student by their ID"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        print(f"Student with ID {student_id} not found.")
        return None
    
    def display_all_students(self):
        """Display all students and their grades"""
        if not self.students:
            print("\nNo students enrolled in the course.")
        else:
            print(f"\nStudents in {self.course_name}:")
            for student in self.students:
                student.display_grades()

def main():
    # Create a course with an instructor
    instructor = Instructor("Dr. Smith", "Python Programming 101")
    
    while True:
        # Display menu
        print("\n=== Online Course Management System ===")
        print(f"Course: {instructor.course_name}")
        print(f"Instructor: {instructor.name}")
        print("\n1. Add new student")
        print("2. Assign grade")
        print("3. Display all students and grades")
        print("4. Display specific student's grades")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            # Add a new student
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            if instructor.add_student(name, student_id):
                print(f"Student {name} added successfully!")
                
        elif choice == '2':
            # Assign a grade
            if not instructor.students:
                print("No students enrolled yet!")
                continue
                
            print("\nCurrent students:")
            for student in instructor.students:
                print(f"- {student}")
                
            student_id = input("Enter student ID: ")
            assignment_name = input("Enter assignment name: ")
            try:
                grade = float(input("Enter grade (0-100): "))
                if 0 <= grade <= 100:
                    if instructor.assign_grade(student_id, assignment_name, grade):
                        print("Grade assigned successfully!")
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid numerical grade.")
                
        elif choice == '3':
            # Display all students
            instructor.display_all_students()
            
        elif choice == '4':
            # Display specific student's grades
            student_id = input("Enter student ID: ")
            student = instructor.find_student(student_id)
            if student:
                student.display_grades()
                
        elif choice == '5':
            print("Thank you for using the Online Course Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the program if this file is run directly
if __name__ == "__main__":
    main()