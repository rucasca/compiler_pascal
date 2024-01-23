#!/usr/bin/env python

import string
import sys
######################################################################################
##
##  Define varias clases que definen cada uno de los diferentes componentes lexicos
##
##
##
######################################################################################

# Clase generica que define un componente lexico 
class Componente:
  def __init__(self):
    self.cat= str(self.__class__.__name__)

 #este metodo mostrará por pantalla un componente lexico
  def __str__(self):
    s=[]
    for k,v in self.__dict__.items():
      if k!= "cat": s.append("%s: %s" % (k,v))
    if s:
      return "%s (%s)" % (self.cat,", ".join(s))
    else:
      return self.cat

#definicion de las clases que representan cada uno de los componentes lexicos

#Algunas tendran camps adicionales para almacenar informacion importante (valor de un numero, etc)

#clases para los simbolos de puntuacion y operadores

class OpAsigna (Componente):
 def __init__(self,nl):
   super().__init__()
   self.linea=nl
   

# Clase que define la categoria OpAdd
class OpAdd(Componente):
  def __init__(self,tipo,nl):
    super().__init__()
    self.tipo=tipo
    self.linea=nl
#debe almacenarse de que operador se trata

# Clase que define la categoria OpMult
class OpMult(Componente):
  def __init__(self,tipo,nl):
    super().__init__()
    self.tipo=tipo
    self.linea=nl
#Debe alnmacenarse que operador es

#clases para representar los numeros.
#Clase que almacena componenetes numericos, tanto enteros como reales
#Para distinguir entre ambos, tambien almacena el tipo en su atributo booleano Real
class Numero (Componente):
  def __init__(self,valor,linea,real):
    super().__init__()
    self.valor= valor
    if(real):
      self.tipo="Real"
    else:
      self.tipo="Entero"
    self.linea=linea
  
#clases para representar los identificadores y palabras reservadas
class Identif (Componente):
  def __init__(self,v,nl):
    super().__init__()
    self.valor= v
    self.linea=nl

#Clase que reprresenta las palabras reservadas.
#Sera una clase independiente de los identificadores para facilitar el analisis sintactico
class PR(Componente):
  def __init__(self, v,nl):
    super().__init__()
    self.valor=v
    self.linea=nl
   #Completar

# Clase que define la categoria OpRel
#Debe alnmacenarse que operador es concretamente

class OpRel (Componente):
  def __init__(self,val,nl):
    super().__init__()
    self.val= val
    self.linea=nl

#Clase para definir los simbolos
class Simbolo(Componente):
  def __init__(self,ch,nl):
    super().__init__()
    self.valor=ch
    self.linea=nl

class EOF(Componente):
  def __init__(self):
    super().__init__()

