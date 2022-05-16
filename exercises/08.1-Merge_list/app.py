chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    empty=[]
    for i in range(len(chunk_one)):
        empty.append(chunk_one[i])
    for i in range(len(chunk_two)):
        empty.append(chunk_two[i])
    return empty
    
print(merge_list(chunk_one, chunk_two))
