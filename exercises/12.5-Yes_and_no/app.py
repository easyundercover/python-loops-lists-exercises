theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

new_list = list(map(lambda x: "wiki" if x == 1 else "woko", theBools))
print(new_list)

