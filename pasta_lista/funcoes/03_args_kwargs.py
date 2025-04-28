def exibur_poema(data_extenso, *args, **kwargs):
    texto ="\n".join(args) # Cria uma string com os versos do poema
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()]) # Cria uma string com os metadados

    mensagem = f"{data_extenso}\n{texto}\n{meta_dados}"
    print(mensagem) # Exibe o poema formatado
   

exibur_poema(
    "Hoje é um dia lindo",  # --------> tupla args
    "Acordei feliz e contente",  # --------> tupla args
    "O sol brilha no céu azul",  # --------> tupla args
    "As flores estão coloridas",  # --------> tupla args  estao dentro de aspa
    autor="daniel da Silva",  # -------->kwargs  olha o que vem depois da virgula
    local="Praia do Leme",  # --------> kwargs
    data="2025-04-25",  # --------> kwargs
)


# A função join() é usada para unir os versos do poema e os metadados em uma única string, separando-os por quebras de linha.
# A função title() é usada para formatar as chaves dos metadados com a primeira letra maiúscula.
# A função print() exibe o poema formatado na tela.

# tupla e usado o as virgulas dentro de um parente  (  "Hoje é um dia lindo",
# "Acordei feliz e contente",  --------> todas essa parte e uma tupla
# "O sol brilha no céu azul",
# "As flores estão coloridas",'')


# quando saber que acabou a tupla e que ela tem que ter uma virgula no final, se não tiver a virgula no final ela não vai ser uma tupla, ela vai ser um argumento só, e não vai funcionar.

# o kwargs  ele comeca quando nao tem mais virgula


# outro exemplo 

# Exemplo com *args (valores posicionais):
#python
#Copiar
#def somar_todos(*numeros):
   # total = 0
   # for numero in numeros:
       # total += numero
   # print(f"Soma total: {total}")

#somar_todos(1, 2, 3, 4, 5)

#Exemplo com **kwargs (valores nomeados):
#def mostrar_informacoes(**dados):
  #  for chave, valor in dados.items():
     #   print(f"{chave}: {valor}")

#mostrar_informacoes(nome="Daniel", idade=26, cidade="Osasco")