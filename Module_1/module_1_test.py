grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

grades[0] = float(sum(grades[0]) / len(grades[0]))
grades[1] = float(sum(grades[1]) / len(grades[1]))
grades[2] = float(sum(grades[2]) / len(grades[2]))
grades[3] = float(sum(grades[3]) / len(grades[3]))
grades[4] = float(sum(grades[4]) / len(grades[4]))

final_list = dict(zip(sorted(students), grades))

print(final_list)