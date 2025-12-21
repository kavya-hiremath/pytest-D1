from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name:keerthi\n"
        "Employee ID:E123\n"
        "Department:Tech\n"
        "Salary:80000"
    )

    assert employee_details("keerthi", "E123", "Tech", 80000) == expected_output
