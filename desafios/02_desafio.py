
def menu():
    menu = f"""
=== MENU ===
[1] \n- Cadastrar novo usuário
[2] \n- Listar usuários
[3] \n- Buscar usuário por CPF
[0] \n- Sair
Escolha uma opção: 1
"""

class Usuario:
    def __novo_usuario__(usuario):
       cpf = input ("digite seu cpf")
        usuario = filtar_usuarios (cpf,usuario):
         
       nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nº - bairro - cidade/estado): ")

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("\n=== Usuário criado com sucesso! ===")

 
# Função para filtrar (buscar) usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


            
        # inicializa os atributos
       

    def exibir_informacoes(self):
        # mostra as informações do usuário
        

def cadastrar_usuario(lista_usuarios):
    # função para cadastrar

def listar_usuarios(lista_usuarios):
    # função para listar

def buscar_usuario(lista_usuarios):
    # função para buscar

# Programa principal:
# loop while com o menu de opções
