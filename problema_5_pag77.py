c=0
with open("input.txt","r",encoding="utf8") as f:
    for i in f.readline():
        if i in ["a","e","i","o","u","ă","î","â"]:
            c+=1
with open("output.txt","a",encoding="utf8") as f2: f2.writelines(str(c))
