# Conheça mais sobre o Regex: https://docs.python.org/pt-br/3.8/howto/regex.html
# Conheça mais sobre o 're' do python: https://docs.python.org/pt-br/3/library/re.html

import re  # Módulo de expressões regulares


# Função que valida o número de telefone
def validate_numero_telefone(phone_number):
    # Padrão de telefone: (XX) 9XXXX-XXXX
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"

    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."


# Entrada do usuário
phone_number = input()

# Chamada da função e armazenamento do resultado
result = validate_numero_telefone(phone_number)

# Impressão do resultado
print(result)
