

operation = 0
nbre1 = 0
nbre2 = 0

print ("mandickou")

print ("veuillez choisir l'operation")
print ("1-addition")
print ("2-soustraction")
print ("3-multiplication")
print ("4-division")

operation = input()
nbre1 = input ("entrez la chiffre 1")
nbre2 = input ( "entrez le chifre 2")


if (operation == 1):
    print (nbre1 + nbre2)
elif operation == 2:
    print (nbre1 - nbre2)
elif operation == 3:
    print (nbre1 * nbre2)
elif operation == 4:
    print (nbre1 /nbre2)