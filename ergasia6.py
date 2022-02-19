import random
points_White = 0
points_Black = 0

#φτιάχνω την σκακιέρα μου 8χ8
board = ["*", "*", "*","*","*","*","*","*",
         "*", "*", "*","*","*","*","*","*",
         "*", "*", "*","*","*","*","*","*",
         "*", "*", "*","*","*","*","*","*",
         "*", "*", "*","*","*","*","*","*",
         "*" ,"*", "*","*","*","*","*","*",
         "*" ,"*", "*","*","*","*","*","*",
         "*", "*", "*","*","*","*","*","*",]

for i in range (0,100):
    #τοποθετώ την βασίλισσα τον πύργο και των αξιωματικό σε τυχαίες θέσεις
    position = random.randint(0, 63)
    board[random.randint(0, 63)]='vasilissa'
    board[random.randint(0, 63)]='pirgos'
    board[random.randint(0, 63)]="aksiomatikos"
    #ψάχνω την βασίλισσα
    for j in range(63):

        if board[j]=='vasilissa':
            break

    pyrgos_found = True
    if pyrgos_found:
        #8 το βήμα για να ελέγχω εαν ειναι στην ίδια κάθετο
        for k in range(j,63,8):
            #εαν ειναι πανω απο 63 τότε βγαίνω εκτός σκακιέρας
            if k+8>63:
                break
                #οταν βρεθεί ο πύργος κάνω και τους 2 +1 γιατι απειλουνται και οι 2
            if board[k]=='pirgos':
                pyrgos_found=False
                points_Black = points_Black + 1
                points_White = points_White + 1
                break
#ψάχνω απο όπου βρέθηκε η βασίλισσα προς τα πίσω
    if pyrgos_found:
        for k in range(j,0,-8):
            #εαν ειναι μικροτερο απο 0 θα φυγει απο την σκακιερα
            if k-8<0:
                break
            if board[k]=='pirgos':
                points_Black = points_Black + 1
                points_White = points_White + 1
                pyrgos_found=False
                break
    aksiomatikos_found=True
    if aksiomatikos_found or pyrgos_found:
        #ψάχνω διαγ΄ωνια της σκακιέρας προς τα αριστερά
        for k in range(j,63,7):
            if j==0:
                break
                #εαν φτάσει τέρμα αριστερά σταματα
            if k%8==0:
                break
            if k+8>63:
                break
#εαν βρεθεί ο πύργος σημαινει η βασίλισσα απειλά τον πύργο
            if board[k]=='pirgos':
                points_Black = points_Black + 1
                pyrgos_found=False
            if board[k]=="aksiomatikos":
                points_Black = points_Black + 1
                points_White = points_White + 1
                aksiomatikos_found=False
            if aksiomatikos_found==False and pyrgos_found==False:
                break
#εαν έχει ηδη βρεθεί ο αξιωματικός και ο πύργος τοτε δεν θα μπει
    if aksiomatikos_found or pyrgos_found:
        #ψάχνω διαγώνια προς τα δεξία της σκακιέρας
        for k in range(j,63,9):

            if k+9>63:
                break
                #εαν ειναι τέρμα δεξιά βγαίνει απο το loop
            if k%7==1:
                break
            if board[k]=='pirgos':
                points_Black = points_Black + 1
                pyrgos_found=False
            if board[k]=="aksiomatikos":
                points_Black = points_Black + 1
                points_White = points_White + 1
                aksiomatikos_found=False
            if aksiomatikos_found==False and pyrgos_found==False:
                break
#ψάχνω προς τα πίσω δεξιά της σκακιέρας
    if aksiomatikos_found or pyrgos_found:
        for k in range(j,0,-7):
            if k-7<0:
                break
            if k%7==1:
                break
            if board[k]=='pirgos':
                points_Black = points_Black + 1
                pyrgos_found=False
            if board[k]=="aksiomatikos":
                points_Black = points_Black + 1
                points_White = points_White + 1
                aksiomatikos_found=False
            if aksiomatikos_found==False and pyrgos_found==False:
                break

    if aksiomatikos_found or pyrgos_found:
        #ψάχνω προς τα πίσω αριστερά της σκακιέρας
        for k in range(j,0,-9):
            if k-9<0:
                break
            if  k%8==0:
                break
            if board[k]=='pirgos':
                points_Black = points_Black + 1
                pyrgos_found=False
            if board[k]=="aksiomatikos":
                points_Black = points_Black + 1
                points_White = points_White + 1
                aksiomatikos_found=False
            if aksiomatikos_found==False and pyrgos_found==False:
                break


print(points_White)
print(points_Black)
