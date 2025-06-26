class pessoa :
    def __init__ (self, nome, ano_nascimento):
        self._nome = nome # Atributo protegido
        self._ano_nascimento = ano_nascimento # Atributo protegido
        
    @property
    def nome(self):
        return self._nome        
    
    @property
    def idade(self):
        _ano_atual = 2025
        return _ano_atual - self._ano_nascimento
       
       
pessoa = pessoa("Daniel", 1998)
print(f"nome: {pessoa.nome}  \tidade:{pessoa.idade}")  # Saída: João      