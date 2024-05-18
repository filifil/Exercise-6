my_dict = {0: 19, 1: 33, 2: 18, 3: 30,4:26}
sorted_keys = sorted(my_dict.keys())
sorted_value = sorted(my_dict.values())
new_num = dict()
for i in range(len(my_dict)):
    new_num.update({sorted_keys[i]:sorted_value[i]})
print(new_num)