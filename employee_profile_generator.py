first_name = "Jesse"
last_name = "Varela"
full_name = first_name + ' ' + last_name
address = "123 Main Street"
address += ", Apartment 4B"
employee_age = 35
employee_info = full_name + " is " + str(employee_age) + " years old"
print(employee_info)
experience_years = 9
experience_info = "Experience: " + str(experience_years) + " years"
print(experience_info)
position = "QA Engineer"
salary = 100000
employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}"
print(employee_card)
employee_code = "QAE-2026-JV-001"
department = employee_code[0:3]
print(department)
year_code = employee_code[4:8]
print(year_code)
initials = employee_code[9:11]
print(initials)
last_three = employee_code[-3:]
print(last_three)