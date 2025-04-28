def somar (a, b):
    return a + b

def mult (a, b):
    return a * b

def subtrair (a, b):
    return a - b


def exibir_resultado(funcao, a, b):
    resultado = funcao(a, b)
    print(f'O resultado da operação é: {a} + {b} = {resultado}')
    
exibir_resultado(somar, 10, 20) 
exibir_resultado(subtrair, 50, 20) 
exibir_resultado(mult, 10, 20)  

op = somar 
print(op(10, 20)) # 30