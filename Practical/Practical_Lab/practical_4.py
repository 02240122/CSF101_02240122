array = ["ECE", "EE", "SWE", "WRE", "EG", "ICE", "A", "IT", "CE", "ME"]
new_array = []
array_len = len(array)

for index in range(array_len):
    new_array.append(array.pop().lower())
print(new_array)

array = ["ECE", "EE", "SWE", "WRE", "EG", "ICE", "A", "IT", "CE", "ME"]
new_array = []
array_len = len(array)

index = array_len
for index in range(array_len):
    new_array.append(array.pop())
    index -= 1
print(new_array)

array = ["ECE", "EE", "SWE", "WRE", "EG", "ICE", "A", "IT", "CE", "ME"]
new_array = []
array_len = len(array)

index = array_len - 1
while index >= 0:
    new_array.append(array.pop().lower())
    index -= 1
print(new_array)
