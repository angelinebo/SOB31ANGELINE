# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student is failing.

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: ")) #Angeline converted input() to int(input())

exam_three = int(input("Input exam grade three: ")) #Angeline renamed exam_3 to exam_three and changed str() to int()

grades = [exam_one,exam_two,exam_three] #Angeline fixed syntax error in grades list
sum = 0
for grade in grades: # Angeline changed grade to grades
  sum = sum + grade

avg = sum / len(grades) #Angeline changed grdes to grades

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90: #Angeline added colon in elif statement
    letter_grade = "B"
elif avg >= 70 and avg < 80: #Angeline simplified 'C' grade elif statement
    letter_grade = "C" #Angeline fixed quotes in 'C' grade
elif avg >= 60 and avg <70: #Angeline simplified 'D' grade elif statement
    letter_grade = "D"
else: #Angeline changed elif to else
    letter_grade = "F"

print("Exam: " + str(grades)) #Angeline removed for loop and changed grade to grades

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade == "F": #Angeline fixed syntax for 'F' grade in if statement
    print("Student is failing.") #Angeline added round brackets in print statement
else:
    print("Student is passing.") #Angeline added round brackets in print statement
