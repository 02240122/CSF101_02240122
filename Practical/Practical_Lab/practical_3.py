# first_list = [0,1,2,3,4,5,6,7,8,9]
# inverse_list = []
# list_len =len(first_list)

# for index in range(list_len):
#      inverse_list.append(first_list.pop())
# print(inverse_list)

student_name = ["Karma", "Dorji", "Pema", "Sonam"]
new_name_list = []
list_len = len(student_name) -1

index = list_len

while index >= 0:
    new_name_list.append(student_name.pop())
    index -= 1

print(new_name_list)
