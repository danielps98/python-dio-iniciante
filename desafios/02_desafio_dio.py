def recomendar_plano(consumo_medio):
    
    
    
    if consumo_medio <= 10:
        return "Plano Essencial Fibra - 50Mbps"
    elif consumo_medio <= 20:
        return "Plano Prata Fibra - 100Mbps"
    else:  # consumo_medio > 20
        return "Plano Premium Fibra - 300Mbps"



# Solicita o consumo médio mensal de dados
consumo = float(input("Informe o consumo médio mensal de dados em GB: "))

# Imprime o plano recomendado
print(recomendar_plano(consumo))
