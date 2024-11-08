name = input("Enter student's name: ")
num_subjects = int(input("Enter number of subjects: "))

total_score = 0
for i in range(num_subjects):
    score = float(input(f"Enter score for subject {i+1}: "))
    total_score += score

average_score = total_score / num_subjects

grade = ''
if average_score >= 90:
    grade = 'A'
elif average_score >= 80:
    grade = 'B'
elif average_score >= 70:
    grade = 'C'
elif average_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"\nStudent Name: {name}")
print(f"Average Score: {average_score:.2f}")
print(f"Grade: {grade}")
