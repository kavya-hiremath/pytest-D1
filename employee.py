def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result


if __name__ == "__main__":
    name = "keerthi"
    emp_id = "E123"
    department = "Tech"
    salary = 80000

    print(employee_details(name, emp_id, department, salary))
