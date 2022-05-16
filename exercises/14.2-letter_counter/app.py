par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:
for i in par:
    counts[i] = counts.get(i,0)+ 1
print(counts)

### Esto sale bien pero no ignora los espacios, ver cómo hacer
