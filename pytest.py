from employee import employee_info

def test_employee_info():
    # Sample employee data
    result = employee_info(
        "John Smith",
        101,
        "IT",
        50000
    )

    # Expected output
    expected = (
        "Employee Name: John Smith\n"
        "Employee ID: 101\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    # Validate the result
    assert result == expected