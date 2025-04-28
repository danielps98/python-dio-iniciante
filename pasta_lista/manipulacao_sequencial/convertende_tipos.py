preco = 10.50  # Conversão de número flutuante para inteiro (isso não altera o valor de 'preco' aqui)
print(preco)  # Vai imprimir 10.5
print(type(preco))  # Vai imprimir <class 'float'>

# Para converter o valor de 'preco' em um número inteiro, você usa a função int()
print(int(preco))  # Vai imprimir 10, convertendo o valor de 10.50 para 10

# Conversão de float e string
print(int(1.94444444))  # Vai imprimir 1 (arredonda para baixo)
print(int("11"))  # Vai imprimir 11 (converte a string "11" para o inteiro 11)
print(float(10.10))  # Vai imprimir 10.1 (mantém o valor como float)
print(float(100))  # Vai imprimir 100.0 (converte o inteiro 100 para float)

# Convertendo inteiro para string
valor = 10
valor_str = str(valor)  # Corrigido: conversão de inteiro para string

print(type(valor))  # Vai imprimir <class 'int'>
print(type(valor_str))  # Vai imprimir <class 'str'>

# Operações matemáticas
print(100 / 2)  # Vai imprimir 50.0 (divisão normal, retorna float)
print(100 // 2)  # Vai imprimir 50 (divisão inteira, retorna int)
