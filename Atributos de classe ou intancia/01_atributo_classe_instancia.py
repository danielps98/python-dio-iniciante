class Estudante:
    escola = "DIO"
    
    def __init__(self, nome, matricula):

        self.nome = nome  # Atributo de instância
        self.matricula = matricula  # Atributo de instância 
    def __str__(self) -> str:
        # Método para retornar uma representação em string do objeto
       return f"Estudante: {self.nome}, Matrícula: {self.matricula}, Escola: {Estudante.escola}"


def mostrar_valores(valores):
    for valor in valores:
        print(valor)

aluno_1 = Estudante("João", 1)
aluno_2 = Estudante("betinho", 2)
aluno_3 =Estudante ("pedro da Silva",4)

Estudante.escola = "DIO - Digital Innovation One"  # Modificando o atributo de classe

# Modificando o atributo de instância
aluno_1.matricula = 3  # Modificando o atributo de instância 
mostrar_valores([aluno_1, aluno_2, aluno_3])  # Exibindo os valores dos objetos
