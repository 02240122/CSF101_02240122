import copy
student_percentage = [74, 80, 87, 85, 84, 90, 90]
student_percentage.append("90")  # append
print(student_percentage)

# copy

new_percentage_list = copy.copy(student_percentage)
new_percentage_list[4] = 95
print(new_percentage_list)

# clear and append

student_percentage.clear()
student_percentage.append("100")
print(student_percentage)

# count
student_percentage = [74, 80, 87, 85, 84, 90, 90]
how_many_times = student_percentage.count(90)
print(how_many_times)

# extend
student_percentage = [74, 80, 87, 85, 84, 90, 90]
copy_list = [74, 80, 87, 85, 95, 90, 90, 90]
student_percentage.extend(copy_list)
print(student_percentage)

# index
print(student_percentage.index(87))

# insert
student_percentage = [74, 80, 87, 85, 84, 90, 90]
student_percentage.insert(0, "39")
print(student_percentage)

# remove
student_percentage.remove(74)
print(student_percentage)

# reverse
student_percentage = [74, 80, 87, 85, 84, 90, 90]
student_percentage.reverse()
print(student_percentage)

student_percentage.sort(reverse=True)
print(student_percentage)
