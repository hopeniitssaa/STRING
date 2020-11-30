s1 = str(input("Dati un cuvant :"))
s2 = str(input("Dati un cuvant :"))
s3 = str(input("Dati un cuvant :"))
s4 = str(input("Dati un cuvant :"))
cuvant=""
if (len(s1)>2 and len(s2)>2 and len(s3)>2 and len(s4)>2):
    cuvant+=s1[0:2]+s2[0]+s3[0:3]+s4[0:len(s4)//2]
else:
    print("Dati un cuvant, cu mai mult decat 2 caractere")
print(cuvant)
