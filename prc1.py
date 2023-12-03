import random
x=0
y=0
for i in range(1,100001):
    a=random.randint(0,1)
    if a==1:
        x+=1
    else:
        y+=1

print(f"Heads--> {x}\nTails--> {y}")