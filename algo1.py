def somme_multiples(n):
    somme = 0
    if n>0:
        for i in range(1,n):
            if i%3==0 or i%5==0:
                somme +=i
        return(f"somme = {somme}")
    else:
        return('veuillez entrer un entier positif')
    
def somme_multiples_2(n):
    if n>=0:
        somme = sum(i for i in range(1,n) if i%3==0 or i%5==0)
        return somme
    else:
        return('veuillez entrer un entier positif')

print(somme_multiples_2(10))
print(somme_multiples_2(20))
print(somme_multiples_2(-20))
