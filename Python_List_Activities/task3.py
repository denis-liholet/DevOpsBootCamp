students_results = []
NAME_KEY = 'name'
MARK_KEY = 'mark'

while True:
    student_name = input("Enter student name: ")
    if student_name == "":
        break
    try:
        student_mark = int(input("Enter student mark: "))
    except ValueError:
        print("Please enter an integer.")
        continue
    students_results.append({NAME_KEY: student_name, MARK_KEY: student_mark})

sorted_results = sorted(students_results, key=lambda x: x[MARK_KEY], reverse=True)

top_three_marks = sorted_results[0:3]
bottom_three_marks = sorted_results[-3:]
total_marks = sum(entry['mark'] for entry in sorted_results)
average_mark = total_marks / len(sorted_results)

print("\n=====Results=====")
print("\nTop three marks:")
for item in top_three_marks:
    print(f"Student: {item[NAME_KEY]}, Mark: {item[MARK_KEY]}")

print("\nBottom three marks:")
for item in bottom_three_marks:
    print(f"Student: {item[NAME_KEY]}, Mark: {item[MARK_KEY]}")

print(f"\nAverage mark: {average_mark.__round__(2)}")
