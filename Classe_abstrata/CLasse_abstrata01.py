from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    
    @abstractmethod
    # Classe abstrata ControleRemoto
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    property
    def marca (self):
        return "Samsung"


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        
    def desligar(self):
        print("Desligando a TV")
        
  

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o ar-condicionado")
    def desligar(self):
        print("Desligando o ar-condicionado")   

        property
    def marca(self):
        print("Marca: Samsung") 

controle = ControleTV()

controle.ligar()  # Método ligar da classe ControleRemoto
controle.desligar()  # Método desligar da classe ControleRemoto

controle_ar = ControleArCondicionado()# Classe ControleArCondicionado


controle_ar.ligar()  # Método ligar da classe ControleRemoto
controle_ar.desligar() 
controle_ar.marca()# Método desligar da classe ControleRemoto
