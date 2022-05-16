list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:
def merge_two_list(list):
    odd=[]
    even=[]
    for i in range(len(list)):
        if list[i] % 2 == 0:
            even.append(list[i])
    for i in range(len(list)):
        if list[i] % 2 != 0:
            odd.append(list[i])
    mergeTwoList = odd + even
    return(mergeTwoList)
print(merge_two_list(list_of_numbers))

###Hacer esto de nuevo porque está mal