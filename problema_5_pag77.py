with open("C:/Users/Steff/Documents/Trash/VS/Scoala/Cl XI/input.txt","r",encoding="utf8") as f: 
    for i in f.readline():
        if i in ["a","e","i","o","u","ă","î","â"]:
            print(i, end=" ")
