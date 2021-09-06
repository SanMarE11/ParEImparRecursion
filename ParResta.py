def resta(n):
    if (n>1):
        n-=2
        resta(n)
    elif(n==0):
        print('Numero Par')
    else:
        print("Numero impar")

n=int(input("Ingresa un dato > "))
resta(n)