people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def deletePerson(person_name):
    new_list=[]
    for i in range(len(people)):
        if people[i] != person_name:
            new_list.append(people[i])
    return(new_list)

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))