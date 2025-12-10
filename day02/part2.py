with open('input.txt', 'r') as f:
    lignes = f.readlines()
    
invalids = []

for ligne in lignes:
    i= 0
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
            l = len(num)
            for k in range(2,l + 1) :
                if l % k != 0:
                    continue
                part = l // k
                p = num[:part]


                #  en python 56 * 3 = 565656 
                if p * k == num:
                    invalids.append(int(num))
                    break
                

        i += 1

print(sum(invalids))
