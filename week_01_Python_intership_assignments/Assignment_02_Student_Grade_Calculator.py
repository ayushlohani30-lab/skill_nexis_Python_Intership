def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F (Fail)"

print("--- Student Grade Calculator ---")

# Taking input for 3 core subjects
try:
    math = float(input("Enter marks for Mathematics (out of 100): "))
    science = float(input("Enter marks for Science (out of 100): "))
    english = float(input("Enter marks for English (out of 100): "))

    # Calculating total and average
    total_marks = math + science + english
    average_percentage = round(total_marks / 3,2)

    # Getting the final grade
    final_grade = calculate_grade(average_percentage)

    # Displaying the results
    print("\n--- Results ---")
    print("Total Marks obtained:",total_marks," / 300")
    print("Average Percentage:",average_percentage,"%")
    print("Final Grade:",final_grade)

except ValueError:
    print("Error: Please enter valid numerical marks.") 