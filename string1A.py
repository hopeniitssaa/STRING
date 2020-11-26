s = str(input("Dati un sir de caractere: "))
n=0
for litere in s:
    if litere.isupper ():
        n+=1
print(n)