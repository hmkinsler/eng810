# Write your solution here
total_exam_points = 0
total_exercise_points = 0
students = 0
passing = 0
failing = 0

dis_5 = "  5: "
dis_4 = "  4: "
dis_3 = "  3: "
dis_2 = "  2: "
dis_1 = "  1: "

while True:
    input = input("Exam points and exercises completed: ")

    if input == "":
        break
    else:
        students += 1
        exam_points = int(input[0:2])
        exercise_points = int(input[3::])

        total_exam_points += exam_points
        total_exercise_points += exercise_points
        total_points = total_exam_points + total_exercise_points

        points = exam_points + exercise_points

        if exam_points < 10:
            dis_0 += "*"
            failing += 1
        elif 0 <= points <= 14:
            dis_0 += "*"
            failing += 1
        elif 15 <= points <= 17:
            dis_1 += "*"
            passing += 1
        elif 18 <= points <= 20:
            dis_2 += "*"
            passing += 1
        elif 21 <= points <= 23:
            dis_3 += "*"
            passing += 1
        elif 24 <= points <= 27:
            dis_4 += "*"
            passing += 1
        elif 28 <= points <= 30:
            dis_5 += "*"
            passing += 1

points_average = (total_points/students)
passing_percentage = ((passing/students)*100)
     

print("Statistics:")
print(f"Points average: {points_average:.2f} ")
print(f"Pass percentage:{passing_percentage:.2f}")
print(f"Grade distribution: ")
print(dis_5)
print(dis_4)
print(dis_3)
print(dis_2)
print(dis_1)
print(dis_0)