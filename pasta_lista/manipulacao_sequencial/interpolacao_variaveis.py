nome = "Daniel"
idade = 25
profissao = "Desenvolvedor"
linguagem = "Python"

dados = {
    "nome": nome,
    "idade": idade,
    "profissao": profissao,
    "linguagem": linguagem
}
saldo = 1000.50

# Exemplo de interpolação de variáveis

print ("nome: %s, idade: %d, profissao: %s, linguagem: %s" % (nome, idade, profissao, linguagem))
#essa forma nao e mas utilizada 

print("nome: {}, idade: {}, profissao: {}, linguagem: {}".format(nome, idade, profissao, linguagem))

print("nome: {0}, idade: {1}, profissao: {2}, linguagem: {3}".format(nome, idade, profissao, linguagem))


print("nome: {n}, idade: {i}, profissao: {p}, linguagem: {l}".format(n=nome, i=idade, p=profissao, l=linguagem))

print("nome{nome} :idade {idade} : profissao {profissao} : linguagem {linguagem}".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))


print("nome: {nome}, idade: {idade}, profissao: {profissao}, linguagem: {linguagem}".format(**dados))

print(f"nome: {nome}, idade: {idade}, profissao: {profissao}, linguagem: {linguagem} + saldo: {saldo:.1f}")