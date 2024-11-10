# Employee and Department Management System
# This program implements a basic system for managing employees and departments in a company

class Employee:
    """
    Employee class to represent an employee in the company
    Attributes:
        name: Name of the employee
        employee_id: Unique ID for the employee
        salary: Employee's annual salary
    """
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        """Display employee's details"""
        print(f"\nEmployee Details:")
        print(f"Name: {self.name}")
        print(f"ID: {self.employee_id}")
        print(f"Salary: ${self.salary:,.2f}")
    
    def update_salary(self, new_salary):
        """Update employee's salary"""
        if new_salary > 0:
            self.salary = new_salary
            print(f"Salary updated successfully to ${self.salary:,.2f}")
            return True
        else:
            print("Error: Salary must be greater than 0")
            return False
    
    def __str__(self):
        """String representation of the employee"""
        return f"{self.name} (ID: {self.employee_id})"

class Department:
    """
    Department class to manage employees in a department
    Attributes:
        department_name: Name of the department
        employees: List of employees in the department
    """
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []  # Empty list to store employees
    
    def add_employee(self, name, employee_id, salary):
        """
        Add a new employee to the department
        Returns the created employee object if successful, None if employee ID already exists
        """
        # Check if employee ID already exists
        if any(emp.employee_id == employee_id for emp in self.employees):
            print("Error: Employee ID already exists!")
            return None
        
        # Create and add new employee
        employee = Employee(name, employee_id, salary)
        self.employees.append(employee)
        return employee
    
    def calculate_total_salary(self):
        """Calculate total salary expenditure for the department"""
        total_salary = sum(emp.salary for emp in self.employees)
        return total_salary
    
    def display_total_expenditure(self):
        """Display total salary expenditure for the department"""
        total = self.calculate_total_salary()
        print(f"\nDepartment: {self.department_name}")
        print(f"Total Salary Expenditure: ${total:,.2f}")
        print(f"Number of Employees: {len(self.employees)}")
        if self.employees:
            print(f"Average Salary: ${total/len(self.employees):,.2f}")
    
    def display_all_employees(self):
        """Display all employees in the department"""
        if not self.employees:
            print(f"\nNo employees in {self.department_name} department.")
        else:
            print(f"\nEmployees in {self.department_name} department:")
            for emp in self.employees:
                emp.display_details()
    
    def find_employee(self, employee_id):
        """Find an employee by their ID"""
        for emp in self.employees:
            if emp.employee_id == employee_id:
                return emp
        print(f"Employee with ID {employee_id} not found.")
        return None

def main():
    # Create a department
    dept_name = input("Enter department name: ")
    department = Department(dept_name)
    
    while True:
        # Display menu
        print("\n=== Employee Management System ===")
        print(f"Department: {department.department_name}")
        print("\n1. Add new employee")
        print("2. Update employee salary")
        print("3. Display all employees")
        print("4. Display department expenditure")
        print("5. Display specific employee details")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            # Add a new employee
            name = input("Enter employee name: ")
            employee_id = input("Enter employee ID: ")
            try:
                salary = float(input("Enter employee salary: $"))
                if salary > 0:
                    if department.add_employee(name, employee_id, salary):
                        print(f"Employee {name} added successfully!")
                else:
                    print("Salary must be greater than 0!")
            except ValueError:
                print("Please enter a valid numerical salary.")
                
        elif choice == '2':
            # Update employee salary
            if not department.employees:
                print("No employees in department!")
                continue
                
            print("\nCurrent employees:")
            for emp in department.employees:
                print(f"- {emp}")
                
            employee_id = input("Enter employee ID: ")
            employee = department.find_employee(employee_id)
            if employee:
                try:
                    new_salary = float(input("Enter new salary: $"))
                    employee.update_salary(new_salary)
                except ValueError:
                    print("Please enter a valid numerical salary.")
                
        elif choice == '3':
            # Display all employees
            department.display_all_employees()
            
        elif choice == '4':
            # Display department expenditure
            department.display_total_expenditure()
            
        elif choice == '5':
            # Display specific employee details
            employee_id = input("Enter employee ID: ")
            employee = department.find_employee(employee_id)
            if employee:
                employee.display_details()
                
        elif choice == '6':
            print("Thank you for using the Employee Management System!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# Run the program if this file is run directly
if __name__ == "__main__":
    main()