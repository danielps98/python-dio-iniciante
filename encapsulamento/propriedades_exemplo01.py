class Foo:
    def __init__(self, x=None):
        self._x = x  # Atributo protegido
    
    @property
    def x (self):
        return self._x or 0 
    
    @x.setter
    def x (self, value):
        self._x += value
    
    @x.deleter
    def x (self):
       self._x = 0  # Não é possível deletar, mas podemos redefinir para zero   


foo = Foo (10)
print(foo.x)
del foo.x 
print(foo.x)
foo.x = 10  
print(foo.x) 
