my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:
var = 0
for i in range(len(my_list)):
  if my_list[i] > var:
    var = my_list[i] 
print(var)