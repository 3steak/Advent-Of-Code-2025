# revoir suite arithmétique
new_position = 50
with open('input.txt', 'r') as f:
    lignes = f.readlines()

count = 0

for ligne in lignes:
    ligne = ligne.strip()
    if not ligne:
        continue

    direction = ligne[0]
    deplacement = int(ligne[1:])

    if direction == "R":
        first = (100 - new_position) % 100
        if first == 0:
            first = 100 
        if deplacement >= first:
            count += 1 + (deplacement - first) // 100

        new_position = (new_position + deplacement) % 100

    else:
        first = new_position
        if first == 0:
            first = 100
        if deplacement >= first:
            count += 1 + (deplacement - first) // 100
        new_position = (new_position - deplacement) % 100

print(count)
