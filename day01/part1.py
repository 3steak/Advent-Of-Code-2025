
import re

new_position = int(50)
with open('input.txt', 'r') as f:
    lignes = f.readlines()
count= int(0)
for ligne in lignes:

    plus_ou_moins = re.sub(r'[^a-zA-Z]', '', ligne)
    deplacement = int(re.sub('[^0-9]', '', ligne))
    if plus_ou_moins == "L":
        new_position = (new_position - deplacement)%100
        print (new_position)
        if new_position == 0:
            count += 1
    else:
        new_position = (new_position + deplacement)%100
        print (new_position)
        if new_position == 0:
            count += 1
            
print (count)