class passarinho:

    def voar(self):
       print( "esta voando.")
    
class pardal(passarinho):
    def voar (self):
         print( "pardal está voando.")
    
class avestruz(passarinho):
    def voar (self):
       print( "não voa, mas corre muito rápido")

#exemplo de ruim do uso de hernança 
class aviao(passarinho):
    def voar(self):
       print ("avião está voando com asas de metal.")     
     
def plano_voo(obj):
    obj.voar()
   
p1 = pardal()
p2 = avestruz()
p3 = aviao()
# polimorfismo01.py
     
plano_voo(p1)  # Saída: pardal está voando.
plano_voo(p2)  # Saída: avestruz não voa, mas corre muito rápido.   
plano_voo(aviao())  # Saída: avião está voando com asas de metal.
     