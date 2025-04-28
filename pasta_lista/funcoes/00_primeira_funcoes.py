def exibir_mensagem():
    print("ola mundo python")

def exibir_mensagem_2(nome):
    print(f"Olá {nome}, seja bem-vindo(a) ao sistema de contatos!")


def exibir_mensagem_3(nome="Daniel"):
    print(f"Olá {nome}, seja bem-vindo(a) ao sistema de contatos!")


exibir_mensagem() # tenho que chamar a função para ela ser executada 
# mais tem que ser no canto se deixar  p/dentro vai esta dentro da funcão
     # exibir_mensagem()
     
exibir_mensagem_2 (nome="giovana") #nesse ex: eu estou chamando a função e passando o argumento nome=giovana se eu nao passar o argumento ela vai dar erro pq eu nao chamei a função no inicio
#igualmente no arggumento 3 eu nao preciso passar o argumento nome pq ele ja tem um valor padrão definido na função, se eu quiser passar outro valor eu posso passar, mas se eu não passar ele vai usar o valor padrão que é "Daniel"
#exibir_mensagem_2(nome="Daniel") #se eu passar o argumento nome=Daniel ele vai substituir o valor padrão que é Daniel, e vai ficar "ola Daniel seja bem-vindo ao sistema de contatos"
exibir_mensagem_3()
exibir_mensagem_3(nome="joazinho")
