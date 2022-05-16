arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:
def sumOdds():
    var=0
    for i in (len(arr)):
        if i % 2 != 0:
            var = var + arr[i]
    return var
    
print(sumOdds())

###Hacer esto de nuevo porque está mal

