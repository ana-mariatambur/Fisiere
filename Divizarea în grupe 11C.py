with open("lista11C.txt","rt")as f:
    l=list(f)
n=medie=0
for i in l:
    x=i.split()
    nota=int(x[2])
    n,media=n+1,media+nota
    if x[3]=="1":
        f=open("engleza.txt","a")
        f.write(i)
        f.close()
    else:
        f=open("franceza.txt","a")
        f.write(i)
        f.close()
med=round((media/float(n)),2)
f=open("media.txt","w")
f.write("media clasei:")
f.write(str(med))
f.close()