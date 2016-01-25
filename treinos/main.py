# -* coding: utf-8 -*-
print(0b1),    #1
print(0b10),   #2
print( 0b11),   #3
print( 0b100),  #4
print( 0b101),  #5
print( 0b110),  #6
print( 0b111)   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11

num  = 0b0 #12
mask = 0b1000 #4
"""
num : 0b1100 #12
mask: 0b0100 #4
============
      0b0100 #4
"""
desired = num & mask
print "desired: ",desired
if desired > 0:
    print "O bit estava ativado"

class Square(object):
  def __init__(self):
    self.sides = 4

my_shape = Square()
print my_shape.sides

class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Alo, %s" % (other.name)

class CEO(Employee):
    def greet(self, other):
        print "Volte ao trabalho, %s!" % (other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Alo, Emily
ceo.greet(emp)
# Volte ao trabalho, Steve!

class Triangle(object):
    number_of_sides = 3
    def __init__(self,angle1,angle2,angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        angulos = self.angle1 + self.angle2 + self.angle3
        if angulos != 180:
            return False
        return True

my_triangle = Triangle(90,30,60)
print my_triangle.number_of_sides
print my_triangle.check_angles()

class Point3D(object):
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        """Ao definir uma nova __repr__(), retrone uma string que use as
        variaveis membro da classe para exibir corretamente o ponto 3D.

           Isso diz ao Python para representar este objeto no
           seguinte formato: (x, y, z).
        """
        return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(1,2,3)
print "Meu ponto: ",my_point

# criando um dicionário vazio
dict_empty = {}
print dict_empty

# criando um dicionário com valores
d = {'nome': 'Fernando', 'idade': 27}
print d

# resgatando valor pela chave
print d['nome']

# criando um 'mix' dict
d = {'id': 1, 1: 'id', 'lista': [1, 2, 3, 4]}

print d['lista']
