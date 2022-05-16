my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]
new_list = []

#your code go here:
for i in range(len(my_list)):
    if type(my_list[i]) == type([]):
        new_list.append(my_list[i])
    if type(my_list[i]) == type({}):
        new_list.append(my_list[i])

print(new_list)