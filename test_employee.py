from employee import employee_details
def test_employee_details():
    expected_output = (
        "Employee name: Alex\n"
        "Employee ID:001\n"
        "Department: IT\n"
        "Salary: 55000\n"
    )
    assert employee_details("Alex","001","IT",55000)==expected_output
