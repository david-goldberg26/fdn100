student_row1: dict[str, str] = {'first_name':'vic', 'last_name':'vu', 'course':'python 100'}
student_row2: dict[str, str]  = {'first_name':'david', 'last_name':'goldberg', 'course':'python 100'}
students: list[dict[str, str]] = [student_row1, student_row2]

for row in students:
    print(f"{row['first_name']} {row['last_name']} is registered for {row['course']}")