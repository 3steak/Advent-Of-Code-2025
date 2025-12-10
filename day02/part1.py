with open('input.txt', 'r') as f:
    lignes = f.readlines()
invalids = []
for ligne in lignes:
    i=0
    liste = ligne.split(",")    
    ### a - c, d - g  ###
    while i < len(liste):
    # recuperer a - c puis a et c 
        nbr = liste[i].replace("-", ",")
        nbr = nbr.split(",")
    # print(nbr[0],nbr[1])
    
    #  iterer de a jusque c : a b c
        for num in range(int(nbr[0]),int(nbr[1])+1):
            num = str(num)

            a = num[int(len(num)/2):]
            b = num[:int(len(num)/2)]

            if a == b:
                num = int(num)
                invalids.append(num)
        i+=1

print(sum(invalids))
