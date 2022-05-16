arr = [45, 67, 87, 23, 5,  32, 60]
new_list = []
#your code below:
for i in range((len(arr)-1), -1, -1):
    new_list.append(arr[i])


print(new_list)
#Alternative way:
#arr.reverse()
#print(arr)