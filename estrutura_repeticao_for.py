
vogais = "AEIOU"
texto = input("Digite um texto: ")

#exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in vogais:
        print(letra, end=" ")
 
 
  #exemplo utilizando o range
for numbero in range (0, 51, 5):
    print(numbero, end=" ")
    
