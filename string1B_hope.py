s = str(input("Dati un sir de caractere: "))
n=0
for i in s:
    if ord(i) in range(48,58):
         n+=1
print(n)