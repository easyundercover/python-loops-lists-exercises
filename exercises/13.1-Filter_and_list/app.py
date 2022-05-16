
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def funcion(names):
    return(names.startswith("R"))

resulting_names=list(filter(funcion, all_names))
print(resulting_names)




