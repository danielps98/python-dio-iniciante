linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # Ordena a lista em ordem alfabética
# print(linguagens)  # ["c", "java", "js", "python", "csharp"]
# linguagens = [...]: Cria uma lista com nomes de linguagens de programação.
# linguagens.sort(): Ordena a lista em ordem alfabética crescente, ou seja, de A a Z.


# linguagens.sort(reverse=True)  # Ordena a lista em ordem alfabética reversa
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # Ordena a lista em ordem alfabética espelhada
# print(linguagens)  # ["python", "js", "java", "csharp", "c"]
# linguagens.sort(reverse=True)  # Ordem alfabética inversa (Z → A)


linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # # Ordena pela quantidade de letras
# print(linguagens)  # ["c", "js", "java", "csharp", "python"]

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # Ordena a lista pelo tamanho das strings em ordem decrescente
# print(linguagens)  # ["python", "csharp", "java", "js", "c"]


