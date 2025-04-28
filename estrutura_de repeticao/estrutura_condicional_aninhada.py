conta_normal = True
conta_universitaria = False

saque = 1500
cheque_especial = 2400
saldo = 1000


if conta_normal:
    if saldo >= saque:
        print("Conta normal com saldo positivo.")
        
    elif saque <= (saldo + cheque_especial):
        print("saque normal com cheque especial.")
    else:
        print("saldo insuficiente.")
       
elif conta_universitaria:
    if saldo >= saque:
            print("saque realizado com sucesso.")
            
    else:
        print(" saldo negativo.")
        
else:
    print("sistema nao reconheceu o tipo de conta.")