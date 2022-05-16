spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }
# Your code here
keys = ["love", "code", "smart"]
values = ["amor", "codigo", "inteligente"]

for i in range(len(keys)):
    spanish_translations[keys[i]] = values[i]
  
# Don't touch the code below
print("Translation", spanish_translations["dog"])
print(spanish_translations)

###Mi código hace lo que debería pero no es igual a la solución planteada por 4geeks