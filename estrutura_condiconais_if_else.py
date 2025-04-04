MAIOR_IDADE = 18
IDADE_ESPECIAL =17

idade = int(float(input("Digite sua idade: ")))

if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
    
if idade < MAIOR_IDADE:
    print("Você é menor de idade")
    
    ## if idade >= MAIOR_IDADE: primeiro if
    ## if idade < MAIOR_IDADE: segundo if
    
if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")
    
    ## if idade >= MAIOR_IDADE: primeiro if
    ## else: segundo if
    
if idade >= MAIOR_IDADE:
    print("Você é maior de idade")
    
elif idade == IDADE_ESPECIAL:
    print("Você pode fazer aulas teoricas,mas nao pode fazer aulas práticas")   
    
else:
    print("Você não é maior de idade")
    
    