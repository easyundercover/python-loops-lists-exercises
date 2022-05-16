Celsius_values = [-2,34,56,-10]

def fahrenheit_values(x):
    return (9/5)* x + 32
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
