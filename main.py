from db import create_db, get_db
from employees import add_employee, delete_employee, get_average_salary_by_role


def main():
    running = True
    while running:
        print("Menu:")
        print("1. View employees")
        print("2. Add employee")
        print("3. Delete employee by ID")
        print("4. View average salary by role")
        print("5. Exit")

        choice = get_selection(1, 5)

        if choice == 1:
            employees = get_db()
            print(employees)
        elif choice == 2:
            name = input("Enter employee name: ")
            role = input("Enter employee role: ")
            salary = float(input("Enter employee salary: "))
            id = add_employee(name, role, salary)
            print("Employee added with ID: ", id)
        elif choice == 3:
            id = input("Enter employee ID to delete: ")
            delete_employee(id)
            print(f"Employee with ID {id} deleted.")
        elif choice == 4:
            avg_salaries = get_average_salary_by_role()
            print("Average Salary by Role:")
            for role, salary in avg_salaries.items():
                print(f"{role}: ${salary:.0f}")
        elif choice == 5:
            print("Exiting...")
            running = False


def get_selection(start: int, end: int) -> int:
    while True:
        try:
            i = int(input(f"Select an option ({start}-{end}): "))
            if start <= i <= end:
                return i
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    create_db()
    main()
