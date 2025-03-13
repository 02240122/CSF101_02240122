array = ["ECE", "EE", "SWE", "WRE", "EG", "ICE", "A", "IT", "CE", "ME"]
new_array = []
array_len = len(array)

for index in range(array_len):
    new_array.append(array.pop().lower())
print(new_array)
